import json

def find_city(city_name: str, create_json_bool: bool = False) -> tuple[str, dict]:
    city_dict = []
    
    umlaut_map = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ß": "ss"
    }
    
    def create_json(title: str, dict: dict) -> None:
        with open(f"{title}.json", "w", encoding="utf-8") as f:
            json.dump(dict, f, indent=4)
        print(f"Dict saved in {title}.json")

    def replace_umlauts(text: str) -> str:
        for umlaut, replacement in umlaut_map.items():
            text = text.replace(umlaut, replacement)
        return text

    for table_name, table_data in json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8")).items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                if row["station"] == city_name:
                    # Replace Umlauts in the station name
                    row["station"] = replace_umlauts(row["station"])
                    city_dict.append(row)
    
    if create_json_bool:
        create_json(city_name, city_dict)
    else:
        return city_name, city_dict
