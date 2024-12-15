# Magazine Management System

## Overview
The Magazine Management System is a Python-based application designed to manage magazines, articles, and authors in a relational database. This system enables users to create, save, and retrieve information about magazines, authors, and articles, as well as establish relationships between them. For example, it can associate articles with authors and magazines, providing a structured way to manage content in a magazine publishing environment.

## Features
- **Magazine Management**: Create and manage magazines with specific attributes such as name and category.
- **Author Management**: Add and manage authors with details such as their name.
- **Article Management**: Create articles with attributes like title, content, and associations with authors and magazines.
- **Relational Data**: Retrieve articles associated with a particular magazine, find authors associated with articles, and discover contributing authors to a magazine.
- **Database Management**: Automatically handles database table creation and deletion for magazines, authors, and articles.

## Requirements
- Python 3.12
- SQLite3 (used for database management)

## Installation

1. Clone the repository to your local machine.
2. Navigate into the project directory.
3. run `pipenv install`
4. run `pipenv shell` to jump into the shell.
5. run `python3 app.py` to create and test the database

Ensure you have SQLite3 installed

## Usage

### Models Overview
The system revolves around three key models:
- **Author**: Represents an author, with attributes such as `id` and `name`.
- **Magazine**: Represents a magazine, with attributes such as `id`, `name`, and `category`.
- **Article**: Represents an article, with attributes such as `id`, `title`, `content`, and associations to `author_id` and `magazine_id`.

Each model provides methods to interact with the database, such as saving records, retrieving all records, and creating or deleting database tables.

### Creating and Managing Data
The system allows users to create instances of authors, magazines, and articles and save them to the database. These entities can be linked to each other through their respective IDs (for example, associating an article with an author and a magazine). 

The data models also support methods to retrieve related data, such as fetching all articles written by a particular author or all contributors to a specific magazine.

### Database Table Management
The system can automatically create and delete tables for each model (Author, Magazine, and Article). You can initialize the database by creating tables and manage their structure throughout the application lifecycle.

### Relationships
You can query relationships between authors, articles, and magazines. For instance, the system allows you to retrieve all articles associated with a specific magazine or get all authors who contributed to a particular magazine.

## Example Workflow

1. Create the necessary tables for authors, magazines, and articles.
2. Add authors and magazines by saving them to the database.
3. Create articles that associate an author with a magazine.
4. Retrieve and display articles by magazine or contributors by author.

## Author
This project was created by **Jasper Munene**.

## License
This project is licensed under the MIT License. 
