let car = new Car('AW456', new Account('Andrés Campuzano', 'DOC123'));
car.passenger = 4;
car.printDataCar();

let uberX = new UberX(
	'AW456',
	new Account('Mingyoung', 'KRS453'),
	'Chevrolet',
	'Spark'
);
uberX.passenger = 4;
uberX.printDataCar();
