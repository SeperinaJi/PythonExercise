#Dictionary Exercises

allien_0 = {'color' : 'green', 'points': 5}
print(allien_0['color'])

new_points = allien_0['points']
print("You just earned " + str(new_points) + " points.")

#add key-pair
allien_0['x_position'] = 0
allien_0['y_position'] = 25
print(allien_0)

#modify the key value
allien_0['color'] = 'yellow'
print(allien_0)

#allien moving example
print("Original x-position: "  + str(allien_0['x_position']))
allien_0['speed'] = 'medium'

if allien_0['speed'] == 'slow':
    x_increment = 1
elif allien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

allien_0['x_position'] = allien_0['x_position'] + x_increment
print("New  x-position : " + str(allien_0['x_position']))

allien_0['speed'] = 'fast'
if allien_0['speed'] == 'slow':
    x_increment = 1
elif allien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
allien_0['x_position'] = allien_0['x_position'] + x_increment
print("New  x-position : " + str(allien_0['x_position']))

del allien_0['points']
print(allien_0)

#Exercise of list dictionary
allien_0 = {
    'color' : 'green',
    'points': 5,
}

allien_1 = {
    'color' : 'yellow',
    'points' : 10,
}

allien_2 = {
    'color' : 'red',
    'points' : 15
}

alliens = [allien_0, allien_1, allien_2]
for allien in alliens:
    print(allien)

# Create 30 alliens
alliens = []
for allien_number in range(30):
    new_allien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    alliens.append(new_allien)

for alien in alliens[ : 5]:
    print(alien)

print("Total number of aliens is " + str(len(alliens)))

# modify the first 3 aliens
for alien in alliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in alliens[ : 5]:
    print(alien)