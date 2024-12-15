from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def articles(self):
        from models.article import Article
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        connection.close()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]

    def magazines(self):
        from models.magazine import Magazine
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.* 
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        connection.close()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines]

    @classmethod
    def create_table(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()

    @classmethod
    def drop_table(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS authors")
        connection.commit()
        connection.close()

    @classmethod
    def all(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        connection.close()
        return [cls(author['id'], author['name']) for author in authors]
