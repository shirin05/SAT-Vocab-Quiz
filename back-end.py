import sqlite3
import csv

# connecting to SQlite database
conn = sqlite3.connect('word_definition.db')
c = conn.cursor()

# creating table
c.execute('''
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        definition TEXT NOT NULL
    )
''')

# opens word-list.csv and inserts that data into table
with open('word-list.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row, it's just title word and defintion
    for row in reader:
        c.execute('INSERT INTO words (word, definition) VALUES (?, ?)', (row[0], row[1]))

# commits changes and closes the connection
conn.commit()
conn.close()

        