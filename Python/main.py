from car import Car
from account import Account

if __name__=="__main__":
   print("Test py")

   car = Car("AMS234", Account("Andres Campuzano", "AND876"))
   print(vars(car))
   print(vars(car.driver))
