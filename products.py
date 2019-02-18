products = []
with open('products.csv', 'r') as f: #encoding = 'utf-8'
    for line in f:
        if '商' in line:
            continue
        s = line.strip().split(',')
        name = s[0]
        price = s[1]
        # name, price = line.strip().split(',')
        products.append([name, price])
        print(s)
print(products)
        
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    p = []
    p.append(name)
    p.append(price)
    # p = [name, price]
    products.append(p)
    # products.append([name, price])
print(products)

# print(products[0][0])

for p in products:
    print(p)
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f: #encoding = 'utf-8'
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')