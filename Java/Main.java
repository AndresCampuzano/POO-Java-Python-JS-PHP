package Java;

class Main {
   public static void main(String[] args) {
      System.out.println("Test from Java");
      Car car = new Car("ABC123", new Account("Andrés Campuzano", "ID123"));
      car.passenger = 4;
      car.printDataCar();

      Car car2 = new Car("DEF456", new Account("Mingyoung", "KR456"));
      car2.passenger = 3;
      car2.printDataCar();
   }
}