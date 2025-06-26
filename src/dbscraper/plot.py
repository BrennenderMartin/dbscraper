import json
import re
import matplotlib.pyplot as plt

def summing(counts):
    sum = 0
    for value in counts:
        sum += value
    return sum

def delay_in_minutes(key, counts):
    if key == "early":          return f"Early ({counts[key]})"
    elif key == "no_delay":     return f"On time ({counts[key]})"
    elif key == "full_delay":   return f"Over 3 hours ({counts[key]})"
    elif key == "1_delay":      return f"1 minute ({counts[key]})"
    elif key == "2_delay":      return f"2 minutes ({counts[key]})"
    elif key == "3_delay":      return f"3 minutes ({counts[key]})"
    elif key == "4_delay":      return f"4 minutes ({counts[key]})"
    elif key == "5_delay":      return f"5 minutes ({counts[key]})"
    elif key == "6_delay":      return f"6 minutes ({counts[key]})"
    elif key == "7_delay":      return f"7 minutes ({counts[key]})"
    elif key == "8_delay":      return f"8 minutes ({counts[key]})"
    elif key == "9_delay":      return f"9 minutes ({counts[key]})"
    elif key == "10_delay":     return f"10 minutes ({counts[key]})"
    elif key == "20_delay":     return f"Below 20 minutes ({counts[key]})"
    elif key == "30_delay":     return f"Below 30 minutes ({counts[key]})"
    elif key == "60_delay":     return f"Below 1 hour ({counts[key]})"
    elif key == "120_delay":    return f"Below 2 hours ({counts[key]})"
    elif key == "180_delay":    return f"Below 3 hours ({counts[key]})"
    else:                       return f"Other ({counts[key]})"

def create_plot(json_path="./delay_summary.json"):
    # Load data from JSON file
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    categories = list(data.keys())
    counts = list(data.values())
    sum = summing(counts)
    # Map categories to delay minutes labels
    new_labels = [delay_in_minutes(key, data) for key in categories]
    x = range(len(categories))
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(x, counts)
    plt.xlabel("Delay (in minutes)")
    plt.ylabel("Count")
    plt.title(f"Analysed {sum} items")
    plt.xticks(x, new_labels, rotation=45)
    plt.tight_layout()
    plt.savefig("plot")

if __name__ == "__main__":
    create_plot()
