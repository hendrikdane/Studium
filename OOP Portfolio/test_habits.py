import unittest
from habit import Habit
from analyse import *
from fixtures import create_fixtures
class SimpleTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(1, 1)
class TestHabit(unittest.TestCase):
    def setUp(self):
        """Creates a fresh habit before each test."""
        self.habit = Habit("batting practice", "daily")
    def test_habit_creation(self):
        """Checks that a habit is created with the correct name and periodicity."""
        self.assertEqual(self.habit.name, "batting practice")
        self.assertEqual(self.habit.periodicity, "daily")
    def test_complete(self):
        """Checks that completing a habit adds one entry to completions."""
        self.habit.complete(note="10x curveballs", with_teammate="Jake")
        self.assertEqual(len(self.habit.completions), 1)
    def test_add_excuse(self):
        """Checks that logging an excuse adds one entry to excuses."""
        self.habit.add_excuse(excuse="sick")
        self.assertEqual(len(self.habit.excuses), 1)
        
class TestAnalytics(unittest.TestCase):
    def setUp(self):
        """Loads fixture habits before each test."""
        self.habits = create_fixtures()
    def test_get_all_habits(self):
        """Checks that all 5 habits are returned."""
        self.assertEqual(len(get_all_habits(self.habits)), 5)
    def test_get_habits_by_periodicity_daily(self):
        """Checks that filtering for daily returns exactly 3 habits."""
        daily = get_habits_by_periodicity(self.habits, "daily")
        self.assertEqual(len(daily), 3)
    def test_get_habits_by_periodicity_weekly(self):
        """Checks that filtering for weekly returns exactly 2 habits."""
        weekly = get_habits_by_periodicity(self.habits, "weekly")
        self.assertEqual(len(weekly), 2)
    def test_longest_streak_habit(self):
        """Checks that the streak for a habit is a positive number."""
        streak = get_longest_streak_habit(self.habits[0])
        self.assertGreater(streak, 0)
    def test_longest_streak_all(self):
        """Checks that the habit with the longest streak is returned."""
        best = get_longest_streak_all(self.habits)
        self.assertIsNotNone(best)


if __name__ == "__main__":
    unittest.main()

