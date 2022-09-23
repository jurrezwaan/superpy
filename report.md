## Eerste probleem:
In de code moet ik vaak dezelfde handeling uit voeren zoals bijvoorbeeld het openen en lezen of schrijven van een csv file. Dit heb ik opgelost door van al die handelingen kleine functions te schrijven die ik in andere functies weer kan gebruiken.  
functie voor openen van csv file naar list: 

---
```python
def read_csv_to_list(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        content = list(reader)
        f.close()
        return content
```
---
deze functie gebruik ik dan later weer hier om een table te maken met de `rich module`. Plus nog een geintje om de eurotekens in de table te krijgen. Ik gebruik ook nog een `*` om de `row` uit te pakken. Dit snap ik niet helemaal maar zonder werkte het niet:

---
```python
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
```
---
## Tweede probleem:
Het script een datum meegeven. Ik heb dit opgelost door die datum in een txt file te zetten en die met functions te wijzigen. Omdat ik de ene keer de tijd als `str` moest hebben en de andere keer als `object` heb ik de functie 2 opties gegeven. `False` voor `object` en `True` voor `str`. Om alleen de date te krijgen van het datetime object zet ik er nog `.date()` achter:

---
```python
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
```
---
Deze functie gebruik ik later weer om de `experation_date` te checken in mijn jetter van een `sell` functie. Hier een snippet uit die `function`:

---
```python
 elif len(product_list) == 1:
        exp_date_string = product_list[0]['expiration_date']
        exp_date_object = datetime.strptime(
            exp_date_string, '%Y-%m-%d').date()
```
---
Ik vergelijk hier 2 time objects. Het time_object voor de experiation date haal ik uit ` inventory.csv`.

---
## Derde probleem:
En tevens het grootste probleem was de `sell` functie. Daar ben ik de langste tijd mee bezig geweest. Toen ik dacht dat het werkte realiseerde ik me dat een product ook twee keer aanwezig kan zijn en dat je dan de gene moet verkopen met de grootse houdbaarheids datum. Ik heb dit opgelost door eerst te checken of er meer dan 1 van een product zijn en om daarna,  als het er meer dan 1 is, een dictoniary te maken en die te sorten op houdbaarheids datum met gebruik van het geweldige `itemgetter`. Het kan vast vele malen eenvoudiger maar dit is waar ik op uit ben gekomen:

---
```python
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
```
## Tot slot:
Ik heb ontzettend veel van deze opdracht geleerd. Als ik het nu opnieuw zou moeten doen zou ik wel veel dingen anders doen en dat is wel frustrerend want het liefst zou ik helemaal opnieuw beginnen maar dat is vanwege de tijd die ik er nu al in heb gestoken een erg slecht idee.   
</b>
Ik wil wel nog even kwijt dat deze opdracht echt krankzinnig moeilijk is. Het werken met 3 modules waar je nog nooit iets mee hebt gedaan heeft me al ongeveer 1.5 week gekost. Verder vind ik de uitleg van wat het programma nou precies moet doen niet erg duidelijk. Er staat bijvoorbeeld dat je classes moet begrijpen en test moet kunnen schrijven. Ik heb 3 dagen weggegooid met het proberen om alles in classes te krijgen maar kwam hier totaal niet uit. Ook het schrijven van testen is dusdanig ingewikkeld dat als ik dat had gedaan ik nog 2 weken nodig had gehad. Uiteindelijk ben ik wel tevreden met het resultaat want volgens mij werkt het!