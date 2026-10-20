from habit import Habit
from tracker import HabitTracker
from analyse import *
from database import save_habits, load_habits
from fixtures import create_fixtures

def main():
    """
    Runs the Base-Track CLI application.
    Loads exsting habits, displays the main menu and handles user input.
    """
    tracker = HabitTracker()
    habits = load_habits()
    
    if not habits:
        habits = create_fixtures()
    
    for h in habits:
        tracker.add_habit(h)
    
    while True:
        print("\n--- Habit Tracker ---")
        print("Enter the respective number!")
        print("1.Add a new habit")
        print("2.Complete a habit.")
        print("3.Log an excuse.")
        print("4.Delete a habit.")
        print("5.Analyse habits.")
        print("6.Exit.")
        choice = input("Choose: ")
        if choice == "6":
            save_habits(tracker.get_habits())
            break
        elif choice == "1":
            name = input("Habit name:")
            periodicity = input("Daily or weekly:")
            new_habit = Habit(name, periodicity)
            tracker.add_habit(new_habit)
            print(f"{name} has been added!")
        elif choice == "2":
            for idx, h in enumerate(habits):
                print(f"{idx + 1}. {h.name}")
            chosen_habit = int(input("Choose a number: ")) - 1
            habit = habits[chosen_habit]
            note = input("If applicable enter a note:")
            teammate = input("Did you do the exercise alone or together? If together enter the name of your team mate.")
            habit.complete(note=note, with_teammate=teammate)
            print(f"{habit.name} completed!")
        elif choice == "3":
            for idx, h in enumerate(habits):
                print(f"{idx + 1}. {h.name}")
            excuse_for = int(input("Choose for which activity you want to log an excuse: ")) - 1
            habit = habits[excuse_for]
            excuse = input("Enter excuse here: ")
            habit.add_excuse(excuse=excuse)
            print(f"Excuse logged for {habit.name}")
        elif choice == "4":
            for idx, h in enumerate(habits):
                print(f"{idx + 1}. {h.name}")
            delete = int(input("Choose which activity you want to delete: ")) - 1
            habit = habits[delete]
            tracker.remove_habit(habit)
            print(f"{habit.name} has been deleted!")
        elif choice == "5":
            print("---Choose the desired analytics-function---")
            print("1. Show all habits")
            print("2. Filter by periodicity")
            print("3. Longest streak (all habits)")
            print("4. Longest streak (specific habit)")
            sub_choice = input("Enter the number: ")
            if sub_choice == "1":
                for h in tracker.get_habits():
                    print(h.name)
            elif sub_choice == "2":
                period_choice = input('Enter "weekly" or "daily": ')
                filtered = get_habits_by_periodicity(tracker.get_habits(), period_choice)
                for h in filtered:
                    print(h.name)
            elif sub_choice == "3":
                result = get_longest_streak_all(tracker.get_habits())
                streak_count = get_longest_streak_habit(result)
                print(f"Longest streak: {result.name} — {streak_count} periods")
            elif sub_choice == "4":
                for idx, h in enumerate(tracker.get_habits()):
                    print(f"{idx + 1}. {h.name}")
                chosen = int(input("Choose habit: ")) - 1
                habit = tracker.get_habits()[chosen]
                print(f"Longest streak: {get_longest_streak_habit(habit)}")
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
