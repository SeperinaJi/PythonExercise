favorite_languages = {
    'jony' : 'ruby',
    'seperina' : 'python',
    'sarah' : 'java',
    'lisa' : 'python'
}

print("Seperina's favorite language is " +
      favorite_languages['seperina'].title()
      +'\n')

for key, value in favorite_languages.items():
    print(key.title() +
          "'s favorite language is " +
          value.title())

python_user = ['seperina']
for name in favorite_languages.keys():
    if name in python_user:
        print("Congrats " +
              name.title() +
              "! Hope you keep studying " +
              favorite_languages[name].title())
    else:
        print("Do you want take Python?")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", please take your poll!")

print("\nThe following laguage has been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#Exercise 6-1

user_information = {
    'first_name' : 'seperina',
    'last_name' : 'ji',
    'age' : 26,
    'city' : 'London'
}

print(user_information)

#Exercise 6-2
favorite_number = {
    'jony' : 4,
    'seperina' : 2,
    'lisa' : 1,
    'cassie' : 6,

}

for key, value in favorite_number.items():

    #number = favorite_number[friend]
    print(key + "'s favorite number is " + str(value))





