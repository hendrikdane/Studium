import json
from datetime import datetime
from habit import Habit
FILE="habits.json"
def habit_to_dict(habit):
    """
    This function transforms a Habit object into a JSON-compatible dictionary.
    """
    return{
        "name": habit.name,
        "periodicity": habit.periodicity,
        "creation_date": str(habit.creation_date),
        "completions": [
            {**c, "date": str(c["date"])} for c in habit.completions
        ],
        "excuses": [
            {**c,"excuse_date": str(c["excuse_date"])} for c in habit.excuses
        ],
    }
def save_habits(habits):
    """
    This function saves a list of habits as a JSON into a file.
    """
    data=[habit_to_dict(h)for h in habits]
    with open(FILE,"w") as f:
        json.dump(data, f)
def dict_to_habit(data):
    """
    This function transforms a dictionary from the JSON-file back into a habit object.
    """
    habit=Habit(data["name"], data["periodicity"])
    habit.creation_date = datetime.fromisoformat(data["creation_date"])
    habit.completions = [{**c, "date": datetime.fromisoformat(c["date"])} for c in data["completions"]]
    habit.excuses= [{**c,"excuse_date": datetime.fromisoformat(c["excuse_date"])} for c in data ["excuses"]]
    return habit
def load_habits():
    """
    This function reads the JSON-file and returns a list of habit objects.
    """
    try:
        with open(FILE,"r") as f:
            data=json.load(f)
            return [dict_to_habit(d) for d in data]
    except FileNotFoundError:
        return[]   
