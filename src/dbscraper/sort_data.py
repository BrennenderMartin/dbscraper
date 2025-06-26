import json

def sort_data(create_json_bool: bool = False) -> tuple[str, dict]:
    def create_json(title: str, dict: dict) -> dict:
        with open(f"{title}.json", "w", encoding="utf-8") as f:
            json.dump(dict, f, indent=4)
        print(f"Dict saved in {title}.json")
    
    delay_dict = {
        "early": 0,
        "no_delay": 0,
        "1_delay": 0,
        "2_delay": 0,
        "3_delay": 0,
        "4_delay": 0,
        "5_delay": 0,
        "6_delay": 0,
        "7_delay": 0,
        "8_delay": 0,
        "9_delay": 0,
        "10_delay": 0,
        "20_delay": 0,
        "30_delay": 0,
        "60_delay": 0,
        "120_delay": 0,
        "180_delay": 0,
        "full_delay": 0,
    }
    
    for table_name, table_data in json.load(open("./src/dbscraper/db.json", "r", encoding="utf-8")).items():
        if table_name != "Stop": continue
        else:
            for row in table_data:
                for key, value in row.items():
                    if key in ["arrival_delay", "departure_delay"]:
                        if value is None: delay_dict["no_delay"] += 1
                        elif value < 0: delay_dict["early"] += 1
                        elif 0 < value <= 1: delay_dict["1_delay"] += 1
                        elif 1 < value <= 2: delay_dict["2_delay"] += 1
                        elif 2 < value <= 3: delay_dict["3_delay"] += 1
                        elif 3 < value <= 4: delay_dict["4_delay"] += 1
                        elif 4 < value <= 5: delay_dict["5_delay"] += 1
                        elif 5 < value <= 6: delay_dict["6_delay"] += 1
                        elif 6 < value <= 7: delay_dict["7_delay"] += 1
                        elif 7 < value <= 8: delay_dict["8_delay"] += 1
                        elif 8 < value <= 9:  delay_dict["9_delay"] += 1
                        elif 9 < value <= 10: delay_dict["10_delay"] += 1
                        elif 10 < value <= 20: delay_dict["20_delay"] += 1
                        elif 20 < value <= 30: delay_dict["30_delay"] += 1
                        elif 30 < value <= 60: delay_dict["60_delay"] += 1
                        elif 60 < value <= 120: delay_dict["120_delay"] += 1
                        elif 120 < value <= 180: delay_dict["180_delay"] += 1
                        elif 180 < value: delay_dict["full_delay"] += 1
    
    if create_json_bool:
        create_json("delay_sorted", delay_dict)
    else:
        return "delay_sorted", delay_dict
