import json

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
            for key, value in row.items():
                if key in ["arrival_delay", "departure_delay"]:
                    if value is not None:
                        this_value = int(value)
                        if this_value >= longest_delay:
                            longest_delay = value
                            long_row = row


def look_for(criteria: dict) -> dict:
    """ This is, what the criteria should look like, if a value cannot be given, leave it at None
    {\n
    "station": string,\n
    "trip_train_number": string,\n
    "trip_train_type": string,\n
    "trip_date": string,\n
    "arrival": string,\n
    "departure": string,\n
    "arrival_delay": int,\n
    "departure_delay": int,\n
    "db_id": string\n
    }
    """
    
    match_score = 0
    match_items = {}
    
    for table_name, table_data in db.items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                
                for key_row, value_row in row.items():
                    for key_crit, value_crit in criteria.items():
                        
                        if key_crit == key_row and value_crit == value_row:
                            print("Oh Junge... Du Hurensohn!")
                        else:
                            print("Noga Boga der SChoggocrossongg fresser!")
                    
    return match_score, match_items

criteria = {
    "station": "Aachen Hbf",
    "trip_train_number": "11",
    "trip_train_type": "ICE",
    "trip_date": "2025-01-13",
    "arrival": "2025-01-13 07:36:00.000000",
    "departure": "2025-01-13 07:39:00.000000",
    "arrival_delay": 10,
    "departure_delay": 10,
    "db_id": "-683349446891373235-2501130623-4"
}

print(f"{longest_delay}\n{long_row}")