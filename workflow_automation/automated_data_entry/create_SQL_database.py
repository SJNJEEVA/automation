import sqlite3                          # import sqlite3 imports Python’s built-in module for working with SQLite databases.

# Connect (creates file if not exists)
conn = sqlite3.connect('automation.db') # sqlite3.connect('automation.db') creates a connection between your Python code and the SQLite database file (automation.db). The argument is the path/filename of the database file. If this file does not exist, it will be created.
cursor = conn.cursor()                  # .cursor() creates a database cursor object. Think of the cursor as a control handle for executing SQL commands and fetching results

# Create a table
cursor.execute('''                      
    CREATE TABLE IF NOT EXISTS requests (   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Amount REAL NOT NULL
    )
''')

# .execute(sql_command, parameters_optional) is used to run SQL commands
    # The first argument is an SQL statement (such as 'SELECT * FROM table' or 'INSERT INTO ... VALUES (?, ?, ?)').
    # You can pass a tuple or list as the second argument for parameterized queries (helps prevent SQL injection).

# CREATE TABLE is SQL command used to create a new table in the database. IF NOT EXISTS is a widely supported SQL clause that tells the database only create the table if it does not already exist. This avoids errors if you run the command multiple times.
    # requests is the name of the table.

# id INTEGER PRIMARY KEY AUTOINCREMENT
    # id is the name of the column and INTEGER means the data type of the column is an integer number & 
        # PRIMARY KEY means this column uniquely identifies each row in the table and A primary key column must have unique values, no duplicates, and cannot be NULL.

# AUTOINCREMENT means the database will automatically assign a unique integer value to this column for every new row inserted, increasing from the last value.

# REAL,TEXT NOT NULL:
    # TEXT is the data type indicating the column will hold string/text data. 
    # REAL - Amount holds a real (decimal) number
    # NOT NULL is a constraint that specifies this column must always have a value; it cannot be left empty or set to NULL.
   

# Insert sample data (if table is empty)
cursor.execute('SELECT COUNT(*) FROM requests') # "SELECT *" means all columns. but in COUNT(*) "*" it means count all rows, not columns
count = cursor.fetchone()[0]                    # .fetchone() returns a single row from the results of a SELECT query as a tuple.
                        
if count == 0:
    sample_data = [
        ('Alice', 'alice@email.com', 100),      # Each tuple in sample_data represents a row to be inserted into the database. The tuple elements correspond to column values.
        ('Bob', 'bob@email.com', 200),
        ('Charlie', 'charlie@email.com', 150),
    ]
    cursor.executemany('INSERT INTO requests (Name, Email, Amount) VALUES (?, ?, ?)', sample_data)   # executemany() will insert each tuple as a new row.
    
    # executemany(sql_command, sequence_of_parameters) allows you to run the same SQL command multiple times with different parameters.
        # You provide the SQL command (like 'INSERT INTO ... VALUES (?, ?, ?)') and a list of tuples with the values to fill in.

    conn.commit()    # .commit() tells SQLite to save (“commit”) any changes you made (like INSERT or UPDATE) to the database file. Until you commit, changes might not be permanent.

cursor.close()
conn.close()
print("Database setup complete with sample data.")


# The cursor is the main interface for executing and controlling operations on the database. Commands like execute, fetch, and updates happen through the cursor, while the connection manages the session and commits changes.

# 'SELECT COUNT(*) FROM requests'
    # SELECT means fetch data.
    # COUNT(*) is a SQL function that returns the number of rows.
    # FROM requests means from the table named requests.

# SQL keyword:
    # SELECT, FROM, WHERE, INSERT INTO, VALUES, UPDATE, DELETE and many others are default SQL keywords. They are part of the SQL language syntax,not Python.   
    # Your .execute() method sends these queries (strings) to the database engine to run.

    # Examples of common SQL keywords you will use inside .execute():
        # CREATE TABLE - SQL command used to create a new table in the database.
        # SELECT — Retrieve data
        # FROM — Specify the table
        # WHERE — Filter condition
        # INSERT INTO — Add new rows
        # VALUES — Specify data for new rows
        # UPDATE — Modify existing rows
        # SET — Specify the new values in UPDATE
        # DELETE FROM — Remove rows
        # CREATE TABLE — Create new tables
        # ALTER TABLE — Change table structure
        # ADD COLUMN - Add an column
        # ORDER BY - Controls the order of rows returned from the database

# 'INSERT INTO requests (Name, Email, Amount) VALUES (?, ?, ?)' - This is also standard SQL syntax for inserting data into a table
    # INSERT INTO requests means "Add new data into the requests table".
    # (Name, Email, Amount) specifies the columns you want to insert data into.
    # VALUES (?, ?, ?) means you will supply 3 values to insert, one for each column.
        # The ? are placeholders for parameterized queries that help prevent SQL injection and make your code cleaner.

    # You use .execute() or .executemany() to run this command with the actual values you want to insert, by passing them as a second argument to .execute() or .executemany().