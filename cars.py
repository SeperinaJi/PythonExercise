cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse = True))
print("\nHere is original list:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is original list:")
print(cars)
print("\nHere is reverse print list:")
cars.reverse()
print(cars)

print("List length is " + str(len(cars)))

# Exercise 3-8/9/10
places = ['china', 'usa', 'uk', 'japan', 'india']
print("\nHere is my places list:")
print(places)
print("\nHere is the sorted places list:")
print(sorted(places))
print("\nHere is the sorted reverse list:")
print(sorted(places, reverse=True))
places.reverse()
print("\nHere is the reverse display:")
print(places)
places.reverse()
print("\nHere is my original list:")
print(places)
places.sort()
print("\n here is my sorted list now")
print(places)
places.sort(reverse=True)
print("\n Here is reverse sorted list now")
print(places)


#Chanpter 5

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())