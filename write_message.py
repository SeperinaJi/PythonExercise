file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love python!\n")
    file_object.write("I love programming!\n")

with open(file_name, 'a') as file_object:
    file_object.write("I also love c!\n")
    file_object.write("I also love creating apps!\n")

with open(file_name) as file_object:
    contents = file_object.read()
print(contents)