import sqlite3
from tabulate import tabulate


CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS reminders (
                    date TEXT,
                    time TEXT,
                    reminder TEXT)
               '''

INSERT_REMINDER = '''INSERT INTO reminders (date, time, reminder) VALUES (:date, :time, :reminder)'''

DELETE_REMINDER_TIME = '''DELETE FROM reminders WHERE date=:date AND time=:time'''

DELETE_REMINDER_NO_TIME = '''DELETE FROM reminders WHERE date=:date'''

CLEAR_ALL = '''DELETE FROM reminders'''

DISPLAY_REMINDERS = '''SELECT * FROM reminders ORDER BY date ASC, time ASC'''

GET_REMINDER = '''SELECT reminder FROM reminders WHERE time=:time'''


def connect():
    return sqlite3.connect("reminder.db")


def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def insert_reminder(connection, cursor, date, time, reminder):
    with connection:
        cursor.execute(INSERT_REMINDER, {"date": date, "time": time, "reminder": reminder})


def delete_reminder_time(connection, cursor, date, time):
    with connection:
        cursor.execute(DELETE_REMINDER_TIME, {"date": date, "time": time})


def delete_reminder_no_time(connection, cursor, date):
    with connection:
        cursor.execute(DELETE_REMINDER_NO_TIME, {"date": date})


def display_reminders(cursor):
    cursor.execute(DISPLAY_REMINDERS)
    reminders = tabulate(cursor.fetchall(), headers=["Date", "Time", "Reminder"])
    return reminders


def get_reminder(cursor, time):
    cursor.execute(GET_REMINDER, {"time": time})
    reminder = cursor.fetchall()[0][0]
    return reminder


def clear_all(connection, cursor):
    with connection:
        cursor.execute(CLEAR_ALL)
