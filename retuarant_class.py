#Exercise 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_reserved = 0


    def describe_restaurant(self):
        print("The " + self.restaurant_name.title() + " restaurant has cuisine :" +
              self.cuisine_type.title())


    def open_restaurant(self):
        print("The " + self.restaurant_name.title() +
              " restaurant is opening.")


    def set_number_served(self, number):
        self.number_reserved = number

    def read_number_served(self):
        print("Current served people number is " + str(self.number_reserved))

    def increment_number_served(self, step):
        self.number_reserved += step


my_restaurant = Restaurant('Hawaii', 'Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.read_number_served()
my_restaurant.set_number_served(5)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(2)
my_restaurant.read_number_served()