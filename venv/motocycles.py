motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# change element in the list
motocycles[0] = 'ducati'
print(motocycles)

# append element to the list as last element
motocycles.append('honda')
print(motocycles)

# insert element to specific index
motocycles.insert(0, 'test')
print(motocycles)

#delete element
del motocycles[0]
print(motocycles)

#delete last element and use it
print("Pop use case: \n")
print (motocycles)
popped_motocycles = motocycles.pop()
print (motocycles)
print (popped_motocycles)

#delete any position element
motocycles.pop(1)
print(motocycles)

# remove use case is for index unknown, only remove the first occur element
motocycles = ['honda' , 'yamaha', 'suzuki', 'ducati']
print (motocycles)

motocycles.remove('ducati')
print (motocycles)

# Exercise 3-4/5/6
guests = ['papa', 'mama', 'sister', 'boyfriend']
print(guests)
print(guests[2].title() + ' cannot attend.')
guests[2] = 'brother'
print (guests)
guests.insert(0, 'uncle')
print (guests)
guests.insert(3, 'jony')
print (guests)
print ("I only invite two person ")
popped_guest = guests.pop()
print ("I am sorry for " + popped_guest)
popped_guest = guests.pop()
print ("I am sorry for " + popped_guest)
popped_guest = guests.pop()
print ("I am sorry for " + popped_guest)
popped_guest = guests.pop()
print ("I am sorry for " + popped_guest)
print (guests[0].title() + " you are invited")
print (guests[1].title() + "  you are invited")
del guests[0]
del guests[1]
print (guests)