#Chapter 8 Function
"""def greeter_user():
    print("Hello!")


greeter_user()

def greeter_user(username):
    print("Hello!" + username.title())

greeter_user('jeese')

def display_message():
    print("I have learned usage of function.")

display_message()

def favorite_book(bookname):
    print("One of my favorite book is " + bookname.title())

favorite_book('steve Jobs')"""


def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name : ")
    if f_name == 'q':
        break

    l_name = input("Last name : ")
    if l_name == 'q':
        break


    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello," + formatted_name + "!")



