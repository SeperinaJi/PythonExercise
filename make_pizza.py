def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping.title())


make_pizza(16, 'mushroom', 'extra cheese')
