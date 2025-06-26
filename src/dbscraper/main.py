import json

db = json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8"))
print(f"Loaded {len(db)} tables from db.json")

longest_delay = 0
long_row = 0

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

delay_dict = {
    "early": 0,
    "no_delay": 0,
    "10_delay": 0,
    "60_delay": 0,
    "180_delay": 0,
    "full_delay": 0,
}

def sort_data(delay_dict):
    for table_name, table_data in db.items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                for key, value in row.items():
                    if key in ["arrival_delay", "departure_delay"]:
                        if value is None:
                            delay_dict["no_delay"] += 1
                        elif value < 0:
                            delay_dict["early"] += 1
                        elif 0 < value <= 10:
                            delay_dict["10_delay"] += 1
                        elif 10 < value <= 60:
                            delay_dict["60_delay"] += 1
                        elif 60 < value <= 180:
                            delay_dict["180_delay"] += 1
                        elif 180 < value:
                            delay_dict["full_delay"] += 1
                            print(value)

def create_json(title, dict):
    with open(f"{title}.json", "w", encoding="utf-8") as f:
        json.dump(dict, f, indent=4)
    print("Delay summary saved in delay_summary.json")

sort_data(delay_dict)
"""
def find_longest_delay(longest_delay, long_row):
    for table_name, table_data in db.items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                for key, value in row.items():
                    if key in ["arrival_delay", "departure_delay"]:
                        if value is not None:
                            this_value = int(value)
                            if this_value >= longest_delay:
                                longest_delay = value
                                long_row = row
    return longest_delay, long_row

delay, row = find_longest_delay(longest_delay, long_row)

print(f"{delay}\n{row}")
"""