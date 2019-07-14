# Exercise list in dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushroom', 'extra cheese', 'pepperoni']

}

print("You ordered a " + pizza['crust'] + "-crist pizza " +
      "With the fllowing toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

#Exercise dictionary in dictionary

users = {
    'jony' : {
        'first': 'jony',
        'last': 'ma',
        'age': 27
    },

    'seperina' :{
        'first': 'seperina',
        'last': 'ji',
        'age': 26
    }

}

for username, userinfo in users.items():
    print('\nUsername:' + username.title())
    full_name = userinfo['first'].title() + " " + userinfo['last'].title()
    age = userinfo['age']

    print("\tFull name : " + full_name)
    print("\tAge is " + str(age))

#Exercise 6-11
cities = {
    'London' : {
        'Country' : 'UK',
        'Population' : 5000,
        'Fact' : 'Captain of UK'
    },

    'Beijing' :{
        'Country' : 'China',
        'Population' : 10000,
        'Fact' : 'Captain of China'
    },

    'New York':{
        'Country': 'America',
        'Population': 10000,
        'Fact': 'Captain of America'

    }

}

for city, city_info in cities.items():
    print('\n City :' + city.title())
    country = city_info['Country']
    population = city_info['Population']
    fact = city_info['Fact']

    print('\t Country: ' +country.title())
    print("\t Population:" + str(population))
    print("\t Fact: " + fact)