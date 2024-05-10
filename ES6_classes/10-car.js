// 10-car.js
class Car {
  // Define private fields
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Method to clone the car object
  cloneCar() {
    const Constructor = this.constructor[Symbol.species] || this.constructor;
    return new Constructor();
  }

  // Symbol.species to return the default constructor
  static get [Symbol.species]() {
    return this;
  }
}

export default Car;
