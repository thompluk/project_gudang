import os
import math

max_pages = None

def table(datas:list, search:str, pages:int):
    data_filtered = []
    if(search != ''):
        data_filtered = [data for data in datas if (search in (data['name']) or (search in data['code']))]
        print(f'Search by: {search}')
    else:
        data_filtered = datas

    end = pages*10
    start = end-10
    data_table = data_filtered[start:end]

    len_filtered = len(data_filtered)
    global max_pages
    max_pages = math.ceil(len_filtered/10)
    len_data = len(data_table)
    if(len_data  != 0):
        column = data_table[0].keys()
        len_col = len(column)
        print('-'*(len_col*22+1))
        for col in column:
            print(f"| {col.upper():<20}", end="")
        print('|')
        print('-'*(len_col*22+1))

        for data in data_table:
            for col in column:
                if type(data[col]) == float:
                    print(f"| {(data[col]):<20,.2f}", end="")
                else:
                    print(f"| {str(data[col])[:20]:<20}", end="")
            print('|')
        print('-'*(len_col*22+1))
        print(f'Pages: {pages}\n')

        if(len_filtered > 10):
            if pages < max_pages: 
                print('[n] Next')
            if pages != 1:
                print('[p] Previous')
        print('[s] Search')
        print('[r] Reset')
        print('[0] Back')

    else:
        print('-'*60)
        print('Data tables not Found !')
        print('-'*60)
        if(search != ''):
            print('[r] Reset')
        print('[0] Back')

def tables(datas:list, menu:str):
    choice = None
    search = ''
    pages = 1
    while choice != '0':
        os.system('cls')
        print(f'\n=== {menu} ===')
        table(datas,search,pages)
        choice = input('Choose Item: ').lower()
        if (choice == '0'):
            break
        elif(choice == 's'):
            search = input('Search keyword (Code or Name): ')
        elif(choice == 'r'):
            search = ''
            pages = 1
        elif(choice == 'n'):
            if pages < max_pages: 
                pages += 1
        elif(choice == 'p'):
            if(pages != 1):
                pages -=1
        elif(len([item for item in datas if(choice.upper() == item['code'])]) != 0):                
            return choice.upper()
        else:
            print('Input is not Valid !')
            input()
