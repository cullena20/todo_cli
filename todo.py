#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import click
import datetime
import database


conn = database.connect()
cur = conn.cursor()
database.create_table(conn)


# returns date with t meaning today and tm meaning tomorrow
def get_date(u_date):
    if u_date == 't':
        current_day = datetime.date.today()
        date = str(datetime.date.strftime(current_day, "%m/%d/%y"))
    elif u_date == 'tm':
        next_day = datetime.date.today() + datetime.timedelta(days=1)
        date = str(datetime.date.strftime(next_day, "%m/%d/%y"))
    else:
        date = u_date
    return date


@click.command(help="Set reminders for yourself in terminal")
@click.option("-c", "--create", nargs=3, type=str,
              help='''Create a reminder. Enter a date, time, and your reminder.
              Enter the reminder in quotes. You can type "t" for today's date or 
              "tm" for tomorrow\'s date. Otherwise, enter the date as MM/DD/YY.''')
@click.option("-s", "--show", is_flag=True,
              help="Displays your reminders.")
@click.option("-d", "--delete", multiple=True, nargs=2, type=str,
              help='''Deletes reminder at specified date and time. Again, you can
              type t for today's date or tm for tomorrow's date. Otherwise enter the
              date as MM/DD/YY. You can enter "a" instead of a time to delete all reminders in
              the specified day''')
@click.option('--clear', is_flag=True,
              help="Clears all reminders.")
def main(create, show, delete, clear):
    if create:
        date = get_date(create[0])
        time = create[1]
        reminder = create[2]
        database.insert_reminder(conn, cur, date, time, reminder)
        click.echo(f"Created reminder on {date} at {time}: {reminder}")
    if show:
        print(database.display_reminders(cur))
    if delete:
        for i, j in delete:
            date = get_date(i)
            if j == 'a':
                database.delete_reminder_no_time(conn, cur, date)
                click.echo(f"Deleted all reminders on {date}")
            else:
                time = j
                reminder = database.get_reminder(cur, time)
                database.delete_reminder_time(conn, cur, date, time)
                click.echo(f"Deleted reminder on {date} at {time}: {reminder}")
    if clear:
        database.clear_all(conn, cur)
        click.echo("Cleared all reminders")


# the default=(None, None) seems to be a weird click thing that I don't fully understand
# is there a better way? works though


if __name__ == "__main__":
    main()
