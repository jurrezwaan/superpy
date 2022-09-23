import csv
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)


def read_csv_to_dict(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        content = list(reader)
        f.close()
        return content


def read_csv_to_list(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        content = list(reader)
        f.close()
        return content


def append_csv(csv_file, list_to_append):
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list_to_append)
        f.close()


def write_csv(csv_file, id):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        L = []
        id = str(id)
        for row in reader:
            if row[0] != id:
                L.append(row)
        f.close()
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(L)
        f.close()


def make_id(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        id = len(list(reader))
        f.close()
        return id


def clear_csv():
    with open('bought.csv', 'w', newline='') as f:
        fieldnames = ['id', 'product_name',
                      'buy_date', 'buy_price', 'expiration_date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        f.close()
    with open('sold.csv', 'w', newline='') as f:
        fieldnames = ['id', 'product_name', 'sell_price', 'sell_date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        f.close()
    with open('inventory.csv', 'w', newline='') as f:
        fieldnames = ['id', 'product_name',
                      'buy_date', 'buy_price', 'expiration_date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        f.close()
    console.print('ALL CSV FILES CLEAR', style='success')
