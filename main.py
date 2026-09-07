# ===================================
# [Warehouse Management]
# ===================================
# Developed by. Thomas Dany Haryanto


# /************************************/

# /===== Import =====/
import os
from items import item_menu
from utils.table import tables

# /===== Data Model =====/
items = [
    {
        'code': 'ITM-0001',
        'name': 'Laptop Lenovo IdeaPad',
        'category': 'Electronics',
        'price': 7500000.0,
        'units': 'pcs',
        'stock': 10
    },
    {
        'code': 'ITM-0002',
        'name': 'Mouse Logitech M331',
        'category': 'Electronics',
        'price': 350000.0,
        'units': 'pcs',
        'stock': 25
    },
    {
        'code': 'ITM-0003',
        'name': 'Keyboard Logitech K120',
        'category': 'Electronics',
        'price': 180000.0,
        'units': 'pcs',
        'stock': 30
    },
    {
        'code': 'ITM-0004',
        'name': 'Monitor LG 24 Inch',
        'category': 'Electronics',
        'price': 2100000.0,
        'units': 'pcs',
        'stock': 8
    },
    {
        'code': 'ITM-0005',
        'name': 'USB Flashdisk 64GB',
        'category': 'Storage',
        'price': 120000.0,
        'units': 'pcs',
        'stock': 40
    },
    {
        'code': 'ITM-0006',
        'name': 'SSD 512GB',
        'category': 'Storage',
        'price': 850000.0,
        'units': 'pcs',
        'stock': 15
    },
    {
        'code': 'ITM-0007',
        'name': 'RAM 8GB DDR4',
        'category': 'Computer Parts',
        'price': 450000.0,
        'units': 'pcs',
        'stock': 20
    },
    {
        'code': 'ITM-0008',
        'name': 'HDMI Cable 2 Meter',
        'category': 'Accessories',
        'price': 75000.0,
        'units': 'pcs',
        'stock': 50
    },
    {
        'code': 'ITM-0009',
        'name': 'Webcam Full HD',
        'category': 'Electronics',
        'price': 550000.0,
        'units': 'pcs',
        'stock': 12
    },
    {
        'code': 'ITM-0010',
        'name': 'Headset Gaming',
        'category': 'Accessories',
        'price': 425000.0,
        'units': 'pcs',
        'stock': 18
    },
    {
        'code': 'ITM-0011',
        'name': 'Printer Epson L3210',
        'category': 'Printer',
        'price': 2300000.0,
        'units': 'pcs',
        'stock': 6
    },
    {
        'code': 'ITM-0012',
        'name': 'Tinta Printer Black',
        'category': 'Printer Supplies',
        'price': 95000.0,
        'units': 'bottle',
        'stock': 35
    },
    {
        'code': 'ITM-0013',
        'name': 'Kertas A4 80gsm',
        'category': 'Office Supplies',
        'price': 55000.0,
        'units': 'ream',
        'stock': 50
    },
    {
        'code': 'ITM-0014',
        'name': 'Kabel LAN Cat6',
        'category': 'Networking',
        'price': 85000.0,
        'units': 'pcs',
        'stock': 30
    },
    {
        'code': 'ITM-0015',
        'name': 'Router TP-Link',
        'category': 'Networking',
        'price': 650000.0,
        'units': 'pcs',
        'stock': 10
    }
]


# /===== Init Variable =====/


# /===== Main Program =====/
def main():
    input_user = None
    while input_user != '0':
        os.system('cls')
        print ('''
=== Warehouse Management ===\n
1. Monitoring Stock
2. Master Item
3. Transaction
4. Report
0. Keluar
        ''')

        input_user = input("Insert your option: ")
        if input_user == "1":
            tables(items, 'MONITORING STOCK')
        elif input_user == "2":
            item_menu(items)
        elif input_user == "3":
            pass
        elif input_user == "4":
            pass
        elif input_user == "0":
            print('Thank you !!!')
            break
        else:
            print("Input is not valid !")
            input()


if __name__ == "__main__":
    main()