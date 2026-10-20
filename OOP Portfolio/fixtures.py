from datetime import datetime, timedelta
from habit import Habit
def create_fixtures():
    """"
    Creates and returns 5 predefined habits 
    with 4 weeks of example tracking data
    for testing purposes. Includes 3 daily 
    and 2 weekly habits.
    """
    batting = Habit("batting practice", "daily")
    stretching_warm_up=Habit("stretching & warm-up","daily")
    watch_game_footage=Habit("watch game footage","daily")
    strength_training=Habit("strength training","weekly")
    review_personal_stats=Habit("review personal stats","weekly")
    habits=[batting,stretching_warm_up,watch_game_footage,strength_training,review_personal_stats]
    for i in range(28):
        if i not in [4,11,19]:
            date=datetime.now()-timedelta(days=28-i)
            batting.completions.append({"date":date, "note":"", "with":""})
    for i in range(28):
        if i not in [6,18,28]:
            date=datetime.now()-timedelta(days=28-i)
            stretching_warm_up.completions.append({"date":date,"note":"","with":""})   
    for i in range(28):
        if i not in [3,5,10]:
            date=datetime.now()-timedelta(days=28-i)
            watch_game_footage.completions.append({"date":date, "note":"","with":""})     
    for i in range(28):
        if i not in [2,8]:
            date=datetime.now()-timedelta(days=28-i)
            strength_training.completions.append({"date":date, "note":"","with":""})  
    for i in range(28):
        if i not in [6]:
            date=datetime.now()-timedelta(days=28-i)
            review_personal_stats.completions.append({"date":date, "note":"","with":""})                                    
    return habits        
