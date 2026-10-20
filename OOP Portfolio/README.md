Base-Track — Habit Tracking App
Base-Track is a simple habit tracking app built with Python. It was created as part of a university portfolio project and allows users to create, manage and analyse their personal habits directly from the command line.

Requirements
Python 3.7 or higher

No additional libraries are required. All modules used are part of Python's standard library.

Installation
Download or clone this repository:
git clone https://github.com/hendrikdane/Studium.git
Navigate to the project folder:
cd "OOP Portfolio"
How to start the app
Run the following command in your terminal:

python main.py
The app will load any existing habits automatically. If no habits are found, it will load 5 predefined example habits to get you started.

How to use the app:
Once started, you will see a menu with the following options:

1. Add a new habit
2. Complete a habit
3. Log an excuse
4. Delete a habit
5. Analyse habits
6. Exit
Simply enter the number of the action you want to perform and follow the instructions on screen.

To add a new habit, select option 1 and enter a name and periodicity (daily or weekly).

To complete a habit, select option 2, choose the habit from the list and optionally add a note or a training partner.

To analyse your habits, select option 5. You can then:

- Show all tracked habits
- Filter habits by periodicity (daily/weekly)
- View the longest streak across all habits
- View the longest streak for a specific habit
All data is saved automatically when you exit the app.

Project structure:
File	           Description
main.py	         Entry point — runs the interactive CLI menu
habit.py	       Defines the Habit class
tracker.py	     Manages the list of habits
analyse.py	     Analytics functions using functional programming
database.py	     Saves and loads habits from a JSON file
fixtures.py	     5 predefined example habits with 4 weeks of data
test_habits.py	 Unit tests for habits and analytics
habits.json	     Auto-generated file where habit data is stored running the unit tests
                          
To run the test suite, use the following command:

python -m unittest test_habits.py
All tests should pass without errors.
