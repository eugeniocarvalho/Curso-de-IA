limitWeight = 3.00
products = {}

for row in open('Products.txt'):
    name, weight, price = row.split(',')

    products.setdefault(name, [])
    products[name] = (float(weight), float(price))

def showProducts(productState):
    i = totalPrice = totalWeight = 0

    print('%15s %10s %10s' % ('Name', 'Weight', 'Price'))
    
    for key, value in products.items():
        if productState[i] == 1:
            print('%15s %10s %10s' % (key, value[0], value[1]))
            totalWeight += value[0]
            totalPrice += value[1]

        i += 1

    print()
    print('%15s %22s' % ('Total weight', 'Total price'))
    print('%15s %22s' % (round(totalWeight, 2), round(totalPrice, 2)))

def fitnessFunction(productState):
    totalPrice = totalWeight = i = 0

    for product, value in products.items():
        if productState[i] == 1:
            totalPrice += float(value[1])
            totalWeight += float(value[0])
        
        i += 1
        
    if totalWeight > limitWeight:
        totalPrice = 1

    return totalPrice