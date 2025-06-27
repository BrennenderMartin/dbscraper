import json

db = json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8"))
print(f"Loaded {len(db)} tables from db.json")

def create_json(title: str, dict: dict) -> None:
    with open(f"{title}.json", "w", encoding="utf-8") as f:
        json.dump(dict, f, indent=4)
    print(f"Dict saved in {title}.json")

def find_koeln_arrival() -> json:
    koeln = []
    koelles = 0
    koelle_start = 0
    for table_name, table_data in db.items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                koelles += 1
                if row["station"] == "Köln Hbf" and row["arrival"] is None:
                    koelle_start += 1
                    row["station"] = "Koeln Hbf"
                    koeln.append(row)
    print(f"{koelles}\n{koelle_start}")
    create_json("koelle_arr", koeln)

def find_koeln():
    koeln = []
    koelles = 0
    for table_name, table_data in db.items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                koelles += 1
                for key, value in row.items():
                    if key == "station" and value == "Köln Hbf":
                        row["station"] = "Koeln Hbf"
                        koeln.append(row)
    print(koelles)
    create_json("koelle", koeln)

def koeln_related():
    koeln_db = json.load(open("./koelle_arr.json", "r", encoding="utf-8"))
    def find_koeln_item(trip_train_number, trip_train_type, trip_date):
        print(trip_train_number, trip_train_type, trip_date)
        for table_data in koeln_db:
            for row in table_data:
                    if row["trip_train_number"] == trip_train_number and row["trip_train_type"] == trip_train_type and row["trip_date"] == trip_date:
                            return row
                    else: return None
                
    berlin_match = {}
    muenchen_match = {}
    hamburg_match = {}
    no_match = {}

    # Convert koeln_db to a dictionary for faster lookups
    koeln_dict = {(row["trip_train_number"], row["trip_train_type"], row["trip_date"]): row for row in koeln_db}

    for table_name, table_data in db.items():
        if table_name != "Stop":
            continue
        for row in table_data:
            key = (row.get("trip_train_number"), row.get("trip_train_type"), row.get("trip_date"))
            if key in koeln_dict:
                if row.get("station") == "Berlin Hbf":
                    berlin_match.update({find_koeln_item(key[0], key[1], key[2]): row})
                elif row.get("station") == "München Hbf":
                    muenchen_match.update({find_koeln_item(key[0], key[1], key[2]): row})
                elif row.get("station") == "Hamburg Hbf":
                    hamburg_match.update({find_koeln_item(key[0], key[1], key[2]): row})
                else:
                    no_match.update({find_koeln_item(key[0], key[1], key[2]): row})
    print(f"{berlin_match}\n{muenchen_match}\n{hamburg_match}\n{no_match}")
    """
    create_json("koelle_berlin_match", berlin_match)
    create_json("koelle_muenchen_match", muenchen_match)
    create_json("koelle_hamburg_match", hamburg_match)
    create_json("koelle_no_match", no_match)
    """



koeln_related()
