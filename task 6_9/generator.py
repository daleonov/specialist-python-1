from collections import defaultdict

f = open(r"C:\Users\daleo\Documents\Специалист\PythonTier1\Задачник\task 6_9\Задача для Питон-1 про товары - Sheet1.csv", encoding = 'utf-8')
f2 = open(r"C:\Users\daleo\Documents\Специалист\PythonTier1\Задачник\task 6_9\out.txt", 'w', encoding = 'utf-8')
header = f.readline()

receipt = defaultdict(list)

md_header = """
Наименование                         | Кол-во |  Цена  | Цена со скидкой
-------------------------------------|-------:|-------:|----------------:
"""

f2.write(md_header)
for line in f:
    rows = line.split(',')
    name = rows[0]
    quantity = float(rows[1])
    if quantity.is_integer():
        quantity = int(quantity)
    price_full = float(rows[2])
    price_discounted = float(rows[3])

    receipt['Наименование'].append(name)
    receipt['Кол-во'].append(quantity)
    receipt['Цена'].append(price_full)
    receipt['Цена со скидкой'].append(price_discounted)
    
    if type(quantity) is float:
        md_line = f'{name.upper():36} | {quantity:6.3f} | {price_full:6.2f} | {price_discounted:6.2f}\n'
    else:
        md_line = f'{name.upper():36} | {quantity:6} | {price_full:6.2f} | {price_discounted:6.2f}\n'
    #print(md_line, end = '')
    f2.write(md_line)

f2.write('\nreceipt = {\n')
for k, v in receipt.items():
    f2.write(f'    \'{k}\': {v},\n')
f2.write('}\n')

f2.close()
