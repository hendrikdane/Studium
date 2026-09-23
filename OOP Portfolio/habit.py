from datetime import datetime
class Habit:
    def __init__(self,name,periodicity):
        """
         Initialises a new Habit with a name and periodicity.
        Creation date is set automatically, completions and excuses start empty.
        """
        self.name= name
        self.periodicity = periodicity
        self.creation_date= datetime.now()
        self.completions=[]
        self.excuses=[]
    def complete(self,note="",with_teammate=""):
        """
        Marks the habit as completed for the current period.
        Optionally logs what was done and who trained alongside.
        """
        entry={
            "date":datetime.now(),
            "note": note,
            "with": with_teammate
        }
        self.completions.append(entry)
    def add_excuse(self,excuse=""):
        """
        This section is responsible for the event that a player cannot exercise a habit.
        It stamps the time of the excuse and allows for the player to insert his excuse. e.g.: "exams", "vacation", "sick".
        """
        entry={
            "excuse_date":datetime.now(),
            "excuse": excuse
        }
        self.excuses.append(entry)
        