from datetime import datetime, date, timedelta
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)


def reset_date():
    with open('datenow.txt', 'w') as f:
        today = date.today()
        date_now = today.strftime('%Y-%m-%d')
        f.write(date_now)
        f.close()
        console.print(f"Date set to: {date_now}", style='success')


def advance_time(days):
    with open('datenow.txt', 'r') as f:
        date_string = f.read()
        tdelta = timedelta(days=days)
        date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
        new_time = date_object + tdelta
        new_date_string = new_time.strftime('%Y-%m-%d')
        f.close()
    with open('datenow.txt', 'w') as f:
        f.write(new_date_string)
        f.close
        console.print(f"Date set to: {new_time}", style='success')


def get_date_as_string(boolean):
    with open('datenow.txt', 'r') as f:
        time_string = f.read()
        if boolean is False:
            time_object = datetime.strptime(time_string, '%Y-%m-%d').date()
            return time_object
        elif boolean is True:
            return time_string
        else:
            console.print('ERROR: expect input True or False', style='error')


def change_date(date):
    with open('datenow.txt', 'w') as f:
        f.write(date)
        f.close
        date_set = datetime.strptime(date, '%Y-%m-%d').date()
        console.print('Date set to {}'.format(date_set), style='success')
