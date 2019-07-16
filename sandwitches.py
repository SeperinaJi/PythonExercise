
#Exercise 7-8, 7-9
print("Pastrami has been sold out!")
sandwitch_orders = ['pastrami','tuna', 'backon', 'pepper', 'pastrami']
finished_sandwitch = []

while sandwitch_orders:
    current_order = sandwitch_orders.pop()
    if current_order != "pastrami":
        finished_sandwitch.append(current_order)
        print("I have made your " + current_order + " sandwitch.")

print("\nI have made following sandwitches:")
for sandwitch in finished_sandwitch:
    print(sandwitch)