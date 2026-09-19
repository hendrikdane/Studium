""""""
Your solution has an analytics module that allows users to analyse their habits. The functionality of this
analytics module must be implemented using the functional programming paradigm. You are free to consider implementing other functionality as well, but these are the minimal requirements. Provide functionality to
- return a list of all currently tracked habits,
- return a list of all habits with the same periodicity,
- return the longest run streak of all defined habits,
- and return the longest run streak for a given habit.
""""""

def get_all_habits(habits):
    return habits
def get_habits_by_periodicity(habits, periodicity):
    return list(filter(lambda h: h.periodicity==periodicity,habits))
def get_longest_streak_habit(habit):
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