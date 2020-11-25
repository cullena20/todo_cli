# To Do List: Command Line Tool
Create reminders for yourself in terminal. You can set reminders at a date and time, show all reminders, and delete reminders. The reminders are stored in an SQL database using sqlite3.

## Commands
You can run ./todo.py followed by some commands with ./ representing the path to the directory containing this folder. To be able to run this anywhere in terminal simply by typing todo, you would have to configure some stuff that I am not sure how to detail here (although I have it configured on my own machine). So without further ado, here are the commands.
* -c/--create <date> <time> <reminder> \
  Type -c or --create followed by a date, time, and reminder to create a reminder. You can write "t" for today's date or "tm" for tomorrow's date. Otherwise write your date as MM/DD/YYYY. Although there will be no errors if you choose to write the date differently, it will be displayed consistently in the database and be ordered correctly. Then write the time in any format you please. Note that you must surround it in quotation marks if there are any spaces. Then write your reminder surrounded by quotation marks. Your reminder will be added to a database and a message will be displayed detailing your action.
* -s/--show \
  Type -s or --show to display your reminders. They will be displayed as a table with columns, date, time, and reminder.
* -d/--delete <date> <time> \
  Delete a reminder at a specified date and time. You can write the date and time the same way as you would when creating a reminder ("t" and "tm" work). If you want to delete all the reminders for a day, write the date followed by "a" in place of time. A message will be displayed detailing your action.
* --clear \
  Type --clear to delete all your reminder. A message will be displayed detailing your action.
  
## Requirements
This script is written for python 3 and uses the built in modules sqlite3 and datetime. It also uses click and tabulate. To download these two modules, run "pip install click" and "pip install tabulate".

## Configuring
You can just download todo.py and database.py, but that's no fun. This tool is meant to run anywhere in terminal by just typing "todo" followed by the commands. To do this you must create a path to the files in .bash_profile. I did this by creating a directory named bin and putting these two files inside of it. I then created (or if you already have one append to it) .bash_profile and wrote 'export PATH=$PATH":$HOME/bin"'. I also ran "mv todo.py todo" so I could simply call todo rather than todo.py.

## Note
This is a project I made for myself and the documentation and organization of this file isn't great. As I continue to learn, I will update this repository to be more formally structured.


