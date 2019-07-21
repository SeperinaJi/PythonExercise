def show_magicaians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['boby', 'lisa', 'cassie']
#show_magicaians(magicians)

def make_great(magicians):
    magicians = ["the Great " + magician for magician in magicians]
    return magicians

magicians = make_great(magicians)
show_magicaians(magicians)