"""Database connection"""
from typing import Any

import mysql.connector

DB_OPTIONS = {
  'host': 'localhost',
  'user': 'root',
  'password': '',
  'database': 'lenew'
}

def write(data: list[dict[str, Any]]) -> int:
    """Write data to database

    Args:
        table: table name
        data: dict with data {category, title, url, preview, date}

    Returns:
        Number of affected rows

    Raises:
        ConnectionError: for SQL errors
    """

    # Check category for resolve duplicates
    on_duplicate = 'ON DUPLICATE KEY UPDATE category=category'
    if data[0].category in ['politics', 'economy']:
        on_duplicate = 'ON DUPLICATE KEY UPDATE url=url'

    # Generate query
    query = ('INSERT INTO "news" (category, title, url, preview, date) '
             'VALUES (%(category)s, %(title)s, %(url)s, %(preview)s, %(date)s) '
             f'{on_duplicate}')

    try:
        connection = mysql.connector.connect(**DB_OPTIONS)
        cursor = connection.cursor()
        cursor.executemany(query, data)
        affected_rows = cursor.rowcount
        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        raise ConnectionError(f'SQL Fail to insert {error}')

    finally:
        if connection.is_connected(): # type: ignore
            connection.close() # type: ignore

    return affected_rows