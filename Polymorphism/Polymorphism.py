

# Parent Class "Motor_Vehicle"
class Motor_Vehicle:
    make = "Honda"
    year = "2019"
    color = "black"
    # Function gets vehicle info
    def getVehicleInfo(self):
        print("The vehicles here are all made by {} in {}, and are all {}.".format(self.make, self.year, self.color))
         

# 1st Child Class "Car"
class Car(Motor_Vehicle):
    model = "Civic"
    wheels = 4
    seats = 5
    # Function gets vehicle info
    def getVehicleInfo(self):
        print("The car is a {} model, so obviously it has {} wheels and {} seats.".format(self.model, self.wheels, self.seats))


# 2nd Child Class "Motorcycle"
class Motorcycle(Motor_Vehicle):
    model = "Gold Wing"
    wheels = 2
    seats = 1
    handlebars = "Ape Hanger"
    # Function gets vehicle info
    def getVehicleInfo(self):
        print("The motorcycle is a {} model. Comes with {} handlebars.".format(self.model, self.handlebars))


# The following invokes the methods inside each class
vehicle = Motor_Vehicle()
vehicle.getVehicleInfo()

car_1 = Car()
car_1.getVehicleInfo()

motorcycle = Motorcycle()
motorcycle.getVehicleInfo()
