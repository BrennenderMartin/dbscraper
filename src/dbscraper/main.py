import json

print("Hello World!")

db = json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8"))
print(f"Loaded {len(db)} tables from db.json")

longest_delay = 0
long_row = 0

for table_name, table_data in db.items():
    print(f"Table: {table_name}")

    if table_name != "Stop":
        print("Skipping table:", table_name)
        continue
    else:
        print("Processing table:", table_name)
        for row in table_data:
            print(row)
            for key, value in row:
                if key == "arrival_delay" or key == "departure_delay":
                    if value > longest_delay:
                        longest_delay = value
                        long_row = row


print(longest_delay)