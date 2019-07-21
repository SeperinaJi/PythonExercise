pets  = ['dog', 'cat', 'goldfish', 'cat', 'cat', 'mouse', 'chicken']


print(pets)
while 'cat' in pets :
    pets.remove('cat')

print(pets)

def describe_pet(pet_name, animal_type= 'dog'):
    """"display animal information"""
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'candy')
describe_pet('dog', 'Willie')

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(pet_name= 'harry')