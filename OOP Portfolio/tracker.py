from habit import Habit
class HabitTracker:
    def __init__(self):
        """
        Initialises the HabitTracker with an empty list of habits.
        """
        self.habits=[]
    def get_habits(self):
        """
        This function is used to fetch existing habits.
        """
        return self.habits
    def add_habit(self,habit):
        """
        This function is used to add new habits to the app.
        """
        self.habits.append(habit)
    def remove_habit(self,habit):
        """
        This function is used to remove a certain habit from the app.
        """
        self.habits.remove(habit)
