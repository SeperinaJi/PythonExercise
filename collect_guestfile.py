file_name = 'guest.txt'

while True:
    print("\nPlease enter 'q' to quit !")
    guest_name = input("Please enter your name: ")
    if guest_name == 'q':
        break
    print(guest_name.title() + ", Welcome you!")

    with open(file_name,'a') as file_object:
        file_object.write(guest_name + '\n')
