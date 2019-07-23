import json

def get_stored_user():
    try:
        file_name = 'username.json'
        with open(file_name) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return user_name

def get_new_user():
    user_name = input("What is your name ?")
    file_name = 'username.json'
    with open(file_name, 'w') as file_object:
        json.dump(user_name, file_object)

    return user_name

def greet_user():
    user_name = get_stored_user()
    if user_name:
        user_check = input("Are you " + user_name.title() + "(y/n)?")
        if user_check == 'y':
           print("Welcome back, " + user_name.title() + "!")
           return

    user_name = get_new_user()
    print("We will remember you when you come back, " + user_name.title() + "!")

greet_user()
