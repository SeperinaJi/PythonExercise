for value in range(1,5):
    print(value)


numbers = list(range(1, 5))
print(numbers)

#min(),max(),sum()

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Exercise 4-3
for value in range(1,21):
    print(value)

#Exercise 4-4
exercise_numbers = list(range(1, 1000001))
print(max(exercise_numbers))
print(sum(exercise_numbers))

#Exercise odd_number
odd_numbers = list(range(1,20,2))
for value in odd_numbers:
    print(value)

# Exercise 4-8
cubes = [ value ** 3 for value in range(1,11)]
print(cubes)


# Exercise 4-7
new_list = []
for value in range (3, 31, 3):
    new_list.append(value)

print(new_list)
