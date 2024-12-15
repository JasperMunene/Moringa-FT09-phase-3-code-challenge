from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'    

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content must be a non-empty string")
        self._content = value

    def save(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        sql_query = """
                INSERT INTO articles (title, content, author_id, magazine_id)
                VALUES (?, ?, ?, ?)
            """
        article_data = (self.title, self.content, self.author_id, self.magazine_id)
        cursor.execute(sql_query, article_data)
        self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def author(self):
        from models.author import Author
        connection = get_db_connection()
        cursor = connection.cursor()
        sql_query = """
                SELECT authors.* 
                FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.id = ?
            """
        cursor.execute(sql_query, (self.id,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return Author(row['id'], row['name'])
        return None

    @property
    def magazine(self):
        from models.magazine import Magazine
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.id = ?
        """, (self.id,))
        row = cursor.fetchone()
        connection.close()
        return Magazine(row['id'], row['name'], row['category']) if row else None

    @classmethod
    def create_table(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                FOREIGN KEY (author_id) REFERENCES authors(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)
            )
        """)
        connection.commit()
        connection.close()

    @classmethod
    def all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles")
        articles = cursor.fetchall()
        connection.close()
        return [cls(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]