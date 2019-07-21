def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('seperina', 'ji')
print(musician)

def build_person(first_name, last_name, age=''):
    person = { 'first' : first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('seperina', 'ji')
print(musician)
