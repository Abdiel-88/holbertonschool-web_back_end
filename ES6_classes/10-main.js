// 10-main.js
import Car from './10-car.js';

// Test class extending Car
class TestCar extends Car {
  // Constructor passes arguments to the Car constructor
  constructor(brand, motor, color) {
    super(brand, motor, color);
  }

  // Clone method that returns an exact copy of the current object
  cloneCar() {
    return new TestCar(this._brand, this._motor, this._color);
  }
}

// Test the cloneCar method
const tc1 = new TestCar('Nissan', 'Turbo', 'Pink');
const tc2 = tc1.cloneCar();

console.log(tc1); // Outputs the original TestCar instance
console.log(tc1 instanceof TestCar); // true

console.log(tc2); // Outputs the cloned TestCar instance
console.log(tc2 instanceof TestCar); // true

console.log(tc1 == tc2); // false (different object instances)
