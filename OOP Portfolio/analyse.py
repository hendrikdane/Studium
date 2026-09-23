def get_all_habits(habits):
    """
    This function returns a list of all currently tracked habits.
    """
    return habits
def get_habits_by_periodicity(habits, periodicity):
    """
    This function filters the habits by their periodicity (daily or weekly)
    and only returns the desired ones.
    """
    return list(filter(lambda h: h.periodicity==periodicity,habits))
def get_longest_streak_habit(habit):
    """
    This function calculates the longest uninterrupted streak 
    for a single habit.
    """
    dates=sorted([entry["date"] for entry in habit.completions])
    streak=1
    longest=1
    for i in range(1, len(dates)):
        diff=(dates[i]- dates[i-1]).days
        if habit.periodicity=="daily" and diff<=1:
            streak+=1
        elif habit.periodicity =="weekly" and diff <=7:
            streak+=1
        else:
            streak=1
        longest=max(longest,streak)     
    return longest       
def get_longest_streak_all(habits):
    """
    This function finds the longest streak of all habits
    and returns it.
    """
    return max(habits, key=lambda h: get_longest_streak_habit(h))