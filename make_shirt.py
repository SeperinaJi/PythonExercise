def make_shirt(size='l',logo= "I love Python"):
    print("You want to print a size " + size.title() + ", logo name is "
          + logo.title())

make_shirt('M', 'Python')
make_shirt(logo='python', size='s')
make_shirt()
