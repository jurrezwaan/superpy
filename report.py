import csv
from wra_csv import read_csv_to_dict, read_csv_to_list
from date_function import get_date_as_string
from datetime import datetime
from operator import itemgetter
from rich.console import Console
from rich.theme import Theme
from rich.table import Table


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)
table_products = Table(show_lines=True, header_style='green')
table_inventory = Table(show_lines=True, header_style='green')
table_sold = Table(show_lines=True, header_style='green')
table_bought = Table(show_lines=True, header_style='green')


def offer_products():
    content = read_csv_to_list('products.csv')
    table_products.add_column('Product Name')
    table_products.add_column('Buy Price')
    table_products.add_column('Sell Price')
    for row in (content[1:]):
        row[1] = '€'+row[1]
        row[2] = '€'+row[2]
        table_products.add_row(*row)
    console.print(table_products)


def report_inventory():
    content = read_csv_to_list('inventory.csv')
    table_inventory.add_column('ID')
    table_inventory.add_column('Product Name')
    table_inventory.add_column('Buy Date')
    table_inventory.add_column('Buy Price')
    table_inventory.add_column('Expiration Date')
    for row in (content[1:]):
        row[3] = '€'+row[3]
        table_inventory.add_row(*row)
    console.print(table_inventory)


def report_sold():
    content = read_csv_to_list('sold.csv')
    table_sold.add_column('ID')
    table_sold.add_column('Product Name')
    table_sold.add_column('Sell Price')
    table_sold.add_column('Sell Date')
    for row in (content[1:]):
        row[2] = '€'+row[2]
        table_sold.add_row(*row)
    console.print(table_sold)


def report_bought():
    content = read_csv_to_list('bought.csv')
    table_bought.add_column('ID')
    table_bought.add_column('Product Name')
    table_bought.add_column('Buy Date')
    table_bought.add_column('Buy Price')
    table_bought.add_column('Expiration Date')
    for row in (content[1:]):
        row[3] = '€'+row[3]
        table_bought.add_row(*row)
    console.print(table_bought)


def sold_today_total():
    content = read_csv_to_dict('sold.csv')
    temp_content = []
    for dict in content:
        getkey = itemgetter('sell_date')
        sell_date_string = getkey(dict)
        sell_date_object = datetime.strptime(
            sell_date_string, "%Y-%m-%d").date()
        if sell_date_object == get_date_as_string(False):
            temp_content.append(float(dict['sell_price']))
    if temp_content == []:
        console.print('No items were sold today', style='error')
        return 0
    with open('temp_'+'sold.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(temp_content)
        f.close()
    content = read_csv_to_list('temp_sold.csv')
    for list in content:
        new_list = [float(i) for i in list]
    console.print('Total sold on {}: €{:.2f}'.format(
        get_date_as_string(True),
        sum(new_list)), style='success')
    return '{:.2f}'.format(sum(new_list))


def bought_today_total():
    content = read_csv_to_dict('bought.csv')
    temp_content = []
    for dict in content:
        getkey = itemgetter('buy_date')
        buy_date_string = getkey(dict)
        buy_date_object = datetime.strptime(
            buy_date_string, "%Y-%m-%d").date()
        if buy_date_object == get_date_as_string(False):
            temp_content.append(float(dict['buy_price']))
    if temp_content == []:
        console.print('No items were bought today', style='error')
        return 0
    with open('temp_'+'bought.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(temp_content)
        f.close()
    content = read_csv_to_list('temp_bought.csv')
    for list in content:
        new_list = [float(i) for i in list]
    console.print('Total bought on {}: €{:.2f}'.format(
        get_date_as_string(True),
        sum(new_list)), style='success')
    return '{:.2f}'.format(sum(new_list))


def profit_today():
    amount_bought = float(bought_today_total())
    amount_sold = float(sold_today_total())
    total = amount_sold - amount_bought
    console.print('Profit on {}: €{:.2f}'.format(
        get_date_as_string(True), total), style='success')


def sold_in_month(year_month):
    content = read_csv_to_dict('sold.csv')
    list_sold = []
    for dict in content:
        getkey = itemgetter('sell_date')
        sell_date = getkey(dict)
        sell_date_to_compare = sell_date[0:-3]
        if sell_date_to_compare == year_month:
            list_sold.append(float(dict['sell_price']))
    if list_sold == []:
        console.print('No items were sold in {}'.format(
            year_month), style='error')
        return 0
    else:
        console.print('Total sold in {}: €{}'.format(
            year_month, sum(list_sold)))
        return '{:.2f}'.format(sum(list_sold))


def bought_in_month(year_month):
    content = read_csv_to_dict('bought.csv')
    list_sold = []
    for dict in content:
        getkey = itemgetter('buy_date')
        buy_date = getkey(dict)
        buy_date_to_compare = buy_date[0:-3]
        if buy_date_to_compare == year_month:
            list_sold.append(float(dict['buy_price']))
    if list_sold == []:
        console.print('No items were bought in {}'.format(
            year_month), style='error')
        return 0
    else:

        console.print('Total bought in {}: €{:.2f}'.format(year_month,
                                                           sum(list_sold)))
        return '{:.2f}'.format(sum(list_sold))


def profit_in_month(year_month):
    sold_amount = float(sold_in_month(year_month))
    bought_amount = float(bought_in_month(year_month))
    console.print('Profit of {}: €{:.2f}'.format(year_month,
                  sold_amount - bought_amount),
                  style='success')
