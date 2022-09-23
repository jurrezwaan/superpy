from date_function import get_date_as_string
from wra_csv import append_csv, make_id
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)


def buy(product_name, buy_price, exp_date):
    id = make_id('bought.csv')
    buy_date = get_date_as_string(True)
    format_buy_price = "{:.2f}".format(buy_price)
    buy_list = [id, product_name, buy_date, format_buy_price, exp_date]
    append_csv('bought.csv', buy_list)
    append_csv('inventory.csv', buy_list)
    console.print("Bought {} for €{} with expiration date: {}".format(
        product_name, format_buy_price, exp_date), style='success')
