requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in  requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

requested_toppings.append('green peppers')
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping)

print("\nFinished making your pizza!")

availabe_toppings = ['mushrooms', 'olive', 'extra cheese', 'pepperoni']

for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry, we don't have " + requested_topping)

#Exercise 5-8

users = ['admin', 'jony', 'lisa']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see the status report?")
        else:
            print("Hello " + user.title() + " thank you for logging in again.")
else:
    print("We need to find some users.")


#Exercise 5-10



current_users = ['liSa', 'jony', 'candy']
current_users_copy = []

for current_user in current_users:
    current_user = current_user.lower()
    current_users_copy.append(current_user)

new_users = ['ben', 'Lisa']

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print("Sorry " + new_user + ", this user name has been taken.")
    else:
        print("You create a new user.")
