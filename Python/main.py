from car import Car

if __name__=="__main__":
   print("Test py")
   car = Car()
   car.license = "ABC123"
   car.driver = "Andres Campuzano"
   print(vars(car))

   car2 = Car()
   car2.license = "DEF456"
   car2.driver = "Mingyoung"
   print(vars(car2))
