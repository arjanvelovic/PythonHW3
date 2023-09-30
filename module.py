def printname(name):
    print(f'Hello {name} ... we have been waiting for you')


cart = {
    'mayo': 95,
    'mustard': 2,
    'moneky': 3,
}

item = 'mooncake'

if item in cart.keys():
    cart[item] += 1
    print(cart)
else:
    cart[item] = 1
    print(cart)

