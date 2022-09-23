from datetime import datetime
from wra_csv import append_csv, write_csv, read_csv_to_dict
from date_function import get_date_as_string
from operator import itemgetter
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)


def sell(product_name, sell_price):
    format_sell_price = "{:.2f}".format(sell_price)
    inventory_list = read_csv_to_dict('inventory.csv')
    if inventory_list == []:
        console.print("ERROR: No items in stock", style='error')
        return
    product_list = []
    for item in inventory_list:
        if item['product_name'] == product_name:
            product_list.append(item)
    if product_list == []:
        console.print("ERROR: Item not in stock", style='error')
    elif len(product_list) == 1:
        exp_date_string = product_list[0]['expiration_date']
        exp_date_object = datetime.strptime(
            exp_date_string, '%Y-%m-%d').date()
        if exp_date_object < get_date_as_string(False):
            console.print(
                "ERROR: Product is expired and tossed in the bin",
                style='error')
            write_csv('inventory.csv', product_list[0]['id'])
        else:
            sell_list = [product_list[0]['id'],
                         product_name, format_sell_price,
                         get_date_as_string(True)]
            append_csv('sold.csv', sell_list)
            write_csv('inventory.csv', sell_list[0])
            console.print('Sold {} for €{}'.format(
                product_name, format_sell_price), style='success')
    elif len(product_list) > 1:
        product_list_sorted = sorted(
            product_list, key=itemgetter('expiration_date'), reverse=True)
        exp_date_string = product_list_sorted[0]['expiration_date']
        exp_date_object = datetime.strptime(
            exp_date_string, '%Y-%m-%d').date()
        if exp_date_object < get_date_as_string(False):
            console.print(
                "ERROR: Product is expired and tossed in the bin",
                style='error')
            write_csv('inventory.csv', product_list[0]['id'])
        else:
            sell_list = [product_list[0]['id'],
                         product_name, format_sell_price,
                         get_date_as_string(True)]
            append_csv('sold.csv', sell_list)
            write_csv('inventory.csv', sell_list[0])
            console.print("Sold {} for €{}".format(
                product_name, format_sell_price), style='success')
