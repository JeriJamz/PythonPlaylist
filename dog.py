#this class
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' is now roll over.')

    
     

#I  classDog( name  age)
my_dog = Dog('Roc', 6)
my_dog.sit()
my_dog.roll_over()


class Restaurant():
    def __init__(self,name,cuisine,avability):
        self.name = name
        self.cuisine = cuisine
        self.avability = avability 

    def describe_restaurant(self):
        print(self.name.title() + ' menu is ' + self.cuisine)

    def open_restaurant(self):
        print(self.name.title() + ' avability is ' + self.avability)


restaurant_1 = Restaurant('Chicken King','10-Peice, Fries','6am-9pm')
restaurant_2 = Restaurant('Kroger', 'Cheesecake','24Hrs')
restaurant_3 = Restaurant('Hunan','Noodles','12am-11am')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()

class Car():
    def __init__(self,millage,year,model,manufacturer):
        self.millage = millage
        self.year = year
        self.model = model
        self.manufacturer = manufacturer

    def car_info(self):
        print('The make and model of the car is: ' + self.model + ' ' + self.manufacturer)

    def odometer(self):
         print('The millage of the car is ' + self.millage)

    def manufactuer(self):
        print('The car was manufactured by ' + self.manufacturer)
    
car_1 = Car('0','2020','Mablibu','Chevy')

car_1.car_info()
car_1.odometer()
car_1.manufactuer()
