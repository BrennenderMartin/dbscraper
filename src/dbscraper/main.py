import json
from sort_data import sort_data
from find_city import find_city

db = json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8"))

def create_json(title, dict):
    with open(f"{title}.json", "w", encoding="utf-8") as f:
        json.dump(dict, f, indent=4)
    print(f"Delay summary saved in {title}.json")

sort_data()
find_city("Münster Hbf")