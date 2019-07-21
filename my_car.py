#from car_class import *
import car_class
car = car_class.Car('audi', 'a4', 2016)
print(car.get_desciptive_name())
car.read_odometer()
car.update_odometer(23)
car.read_odometer()

my_tesla = car_class.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_desciptive_name())
my_tesla.read_odometer()
my_tesla.battery = car_class.Battery(80)
my_tesla.battery.describe_battery()