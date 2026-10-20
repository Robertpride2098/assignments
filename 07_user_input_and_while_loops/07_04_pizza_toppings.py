# pizza toppings
# Robert pride
# Difficulty 5/10

pizzas = True
while pizzas: 
    pizza_topping = input('What toppings would you like on your pizza? ')
    if pizza_topping == 'quit':
        pizzas = False
        print('no more toppings')
    else:
        print(f'We will add {pizza_topping} to your pizza.')