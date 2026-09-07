def get_code(data: list,code:str):
    if len(data) != 0:
        latest = max([int(d['code'][-4:]) for d in data])
        print(latest)
        latest += 1
        return(f"{code}-{latest:04d}")
    else:
        return code+'-0001'

def confirm(text:str):
    res = input(f'Are you sure want to {text}? (yes/no): ' ).lower()
    while res != 'yes' and res != 'no':
        print(res)
        print('Input invalid !')
        res = input(f'Are you sure want to {text}? (yes/no): ' ).lower()
    if res == 'yes':
        return True
    else:
        return False