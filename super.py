# Imports
import argparse
from date_function import reset_date, advance_time, change_date
from buy import buy
from sell import sell
from report import sold_today_total, sold_in_month, bought_in_month, \
    bought_today_total, profit_today, profit_in_month, report_inventory, \
    offer_products, report_sold, report_bought
from wra_csv import clear_csv
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


# gevonden op stackoverflow om spatie van een lege metavar weg te halen
class SingleMetavarHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                parts.extend(action.option_strings)
                parts[-1] += ' %s' % args_string
            return ', '.join(parts)


# top-level parser
parser = argparse.ArgumentParser(prog='SuperPy',
                                 formatter_class=SingleMetavarHelpFormatter,
                                 description='Welcome to the 3Fruits supermarket command line interface')
subparsers = parser.add_subparsers(dest='command')

# options
parser.add_argument(
    '-c',
    '--clear',
    help='clear csv files',
    action='store_true'
)
parser.add_argument(
    '-r',
    '--reset-date',
    help='set date to today',
    action='store_true'
)
parser.add_argument(
    '-a',
    '--advance-time',
    type=int,
    help='advance time with days input: number of days',
    metavar=''
)
parser.add_argument(
    '-i',
    '--input-date',
    help='give set date input: YYYY-MM-DD',
    metavar=''
)

# sub parsers
buy_parser = subparsers.add_parser(
    'buy',
    help='buy product',
    formatter_class=SingleMetavarHelpFormatter,
)
sell_parser = subparsers.add_parser(
    'sell',
    help='sell product',
    formatter_class=SingleMetavarHelpFormatter
)
report_parser = subparsers.add_parser(
    'report',
    help='report cost, revenue and profit',
    formatter_class=SingleMetavarHelpFormatter
)

# buy command
buy_parser.add_argument(
    '-p',
    '--product-name',
    choices=['apple', 'banana', 'pear'],
    help='apple, banana or pear',
    dest='product',
    metavar='',
    required=True
)
buy_parser.add_argument(
    '-b',
    '--buy-price',
    type=float,
    help='give buy price',
    dest='price',
    metavar='',
    required=True
)
buy_parser.add_argument(
    '-e',
    '--expiration-date',
    help='yyyy-mm-dd',
    dest='date',
    metavar='',
    required=True
)

# sell command
sell_parser.add_argument(
    '-p',
    '--product-name',
    choices=['apple', 'banana', 'pear'],
    help='apple, banana or pear',
    dest='product',
    metavar='',
    required=True
)
sell_parser.add_argument(
    '-s',
    '--sell-price',
    type=float,
    help='give buy price',
    dest='price',
    metavar='',
    required=True
)

# report command
report_parser.add_argument(
    '--sold-today',
    action='store_true',
    help='products sold today',
)
report_parser.add_argument(
    '--bought-today',
    action='store_true',
    help='products bought today',
)
report_parser.add_argument(
    '--profit-today',
    action='store_true',
    help='profit of today',
)
report_parser.add_argument(
    '--sold-month',
    type=str,
    help='products sold in month input: YYYY-MM',
    metavar=''
)
report_parser.add_argument(
    '--bought-month',
    type=str,
    help='products bought in month input: YYYY-MM',
    metavar=''
)
report_parser.add_argument(
    '--profit-month',
    type=str,
    help='profit in month input: YYYY-MM',
    metavar=''
)
report_parser.add_argument(
    '--inventory',
    action='store_true',
    help='show inventory',
)
report_parser.add_argument(
    '--sold',
    action='store_true',
    help='show products sold',
)
report_parser.add_argument(
    '--bought',
    action='store_true',
    help='show products bought',
)
report_parser.add_argument(
    '--products',
    action='store_true',
    help='show which products the store has',
)

args = parser.parse_args()


# call functions
if args.command is None:
    if args.clear is True:
        clear_csv()

    elif args.reset_date is True:
        reset_date()

    elif args.advance_time is not None:
        advance_time(args.advance_time)

    elif args.input_date is not None:
        if len(args.input_date) != 10:
            console.print('error: use format YYYY-MM-DD', style="error")
        elif args.input_date[4] != '-':
            console.print('error: use format YYYY-MM-DD', style="error")
        elif args.input_date[7] != '-':
            console.print('error: use format YYYY-MM-DD', style="error")
        else:
            change_date(args.input_date)

    else:
        console.print(
            'error: no arguments given see super.py -h', style='error')

elif args.command == 'buy':
    buy(args.product, args.price, args.date)

elif args.command == 'sell':
    sell(args.product, args.price)

elif args.command == 'report':
    if args.sold_today is True:
        sold_today_total()
    elif args.bought_today is True:
        bought_today_total()
    elif args.profit_today is True:
        profit_today()
    elif args.inventory is True:
        report_inventory()
    elif args.sold is True:
        report_sold()
    elif args.bought is True:
        report_bought()
    elif args.products is True:
        offer_products()
    elif args.sold_month is not None:
        if len(args.sold_month) != 7:
            console.print('error: use format YYYY-MM', style="error")
            exit()
        elif args.sold_month[4] != '-':
            console.print('error: use format YYYY-MM', style="error")
            exit()
        else:
            sold_in_month(args.sold_month)
    elif args.bought_month is not None:
        if len(args.bought_month) != 7:
            console.print('error: use format YYYY-MM', style="error")
            exit()
        elif args.bought_month[4] != '-':
            console.print('error: use format YYYY-MM', style="error")
            exit()
        else:
            bought_in_month(args.bought_month)
    elif args.profit_month is not None:
        if len(args.profit_month) != 7:
            console.print('error: use format YYYY-MM', style="error")
            exit()
        elif args.profit_month[4] != '-':
            console.print('error: use format YYYY-MM', style="error")
            exit()
        else:
            profit_in_month(args.profit_month)
    else:
        console.print(
            'error: option required see report -h for info', style='error')
