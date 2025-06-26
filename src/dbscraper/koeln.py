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
