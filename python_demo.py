import csv 
from datetime import datetime 
 
CSV_FILE="Schedule.csv" 
 
def read_schedule(file_name): 
    schedule = [] 
    with open(file_name, newline='') as F: 
        reader = csv.DictReader(F) 
        for row in reader: 
            schedule.append({ 
                "day": row["day"], 
                "course": row["course"], 
                "time": row["time"], 
                "room": row["room"], 
                "type": row["type"] 
            }) 
    return schedule 
 
def classes_today(schedule): 
    today = datetime.today().strftime("%A") 
    classes = [c for c in schedule if c["day"] == today] 
    return classes 
 
def print_classes(classes): 
    if not classes: 
        print("No classes today!") 
    else: 
        print("Today's Classes and Labs:\n") 
        for c in classes: 
            print(f"- {c['course']} ({c['type']}) at {c['time']} in {c['room']}") 
 
def main(): 
    schedule = read_schedule(CSV_FILE) 
    classes = classes_today(schedule) 
    print_classes(classes) 
 
main() 
