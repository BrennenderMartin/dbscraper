import sqlite3
import json

# Replace 'your_dataset/your_database.db' with the path to your SQLite database file
database_file = 'dbscraper/src/dbscraper/db.sqlite'

# Replace 'output.json' with the name of the output JSON file
output_json_file = 'dbscraper/src/dbscraper/db.json'

# Connect to the SQLite database
conn = sqlite3.connect(database_file)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]

db_data = {}

for table in tables:
    cursor.execute(f'SELECT * FROM "{table}"')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    # Convert rows to list of dicts
    db_data[table] = [dict(zip(column_names, row)) for row in rows]

# Close the cursor and database connection
cursor.close()
conn.close()

# Write all tables to a single JSON file
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(db_data, json_file, indent=4, ensure_ascii=False)

print(f"Data from {database_file} has been successfully converted to {output_json_file}.")