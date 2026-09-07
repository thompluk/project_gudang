import os
from utils.input import get_code
from utils.input import confirm
from utils.table import table
from utils.table import tables

def item_menu(items:list):
    choice = None
    while choice != "0":
        os.system('cls')
        print('''
=== Master Item ===\n
1. Add Item
2. Edit Item
3. Remove Item
0. Keluar
        ''')

        choice = input("Pilih menu: ")

        if choice == "1":
            add_item(items)
            input()
        elif choice == "2":
            edit_item(items)
            input()
        elif choice == "3":
            remove_item(items)
            input()
        elif choice == "0":
            break
        else:
            print("Input is not valid !")
            input()

def add_item(items:list):
    os.system('cls')
    print('\n=== ADD ITEM ===')
    code = get_code(items,'ITM')
    print(f'New Code Procduct: {code}')
    name =      input('Item Name    : ')
    category =  input('Category     : ')
    price =     input('Price        : ')
    units =     input('Units        : ')

    res = confirm('Add Item')

    if(res):
        items.append({
            'code': code
            ,'name': name
            ,'category': category
            ,'price': price
            ,'units': units
            ,'stock': 0
        })
        print(f'\n[!] Item {name} successfully added')
    else:
        print('\n[!] Transaction terminated')

def edit_item(items:list):
    selected_code = tables(items, 'EDIT ITEM')

    # selected_data = next(item for item in items if item['code'] == selected_code) 
    for item in items:
        if item['code'] == selected_code:
            print('\n--Data selected to Edit--')
            print(f'Item Name   : {item['name']}')
            print(f'Category    : {item['category']}')
            print(f'Price       : {item['price']}')
            print(f'Units       : {item['units']}')

            print('\n--Input New Data--')
            name =      input('Item Name    : ')
            category =  input('Category     : ')
            price =     input('Price        : ')
            units =     input('Units        : ')

            res = confirm('Add Item')
            
            if(res):
                item['name'] = name
                item['category'] = category
                item['price'] = price
                item['units'] = units
                print(f'\n[!] Item {item['code']} successfully edited')
                break
            else:
                print('\n[!] Transaction terminated')
                break

def remove_item(items:list):
    selected_code = tables(items, 'REMOVE ITEM')

    for item in items:
        if item['code'] == selected_code:
            print('\n--Data selected to Remove--')
            print(f'Item Name   : {item['name']}')
            print(f'Category    : {item['category']}')
            print(f'Price       : {item['price']}')
            print(f'Units       : {item['units']}')

            res = confirm('Remove Item')
            
            if(res):
                items.remove(item)
                print(f'\n[!] Item {item['code']} successfully removed')
                break
            else:
                print('\n[!] Transaction terminated')
                break

# def edit_item(items:list):
#     choice = None
#     search = ''
#     while choice != '0':
#         os.system('cls')
#         print('\n=== EDIT ITEM ===')
#         table(items,search)
#         choice = input('Choose Item: ').lower()
#         if(choice=='s'):
#             search = input('Search keyword (Code or Name): ')
#         elif(choice=='r'):
#             search = ''
#         elif(item for item in items if(choice == item['code'])):
#             pass
#         else:
#             print('Input is not Valid !')
#             input()
    