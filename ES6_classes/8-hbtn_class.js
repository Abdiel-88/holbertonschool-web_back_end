// 8-hbtn_class.js
export default class HolbertonClass {
  constructor(size, location) {
    // Verify data types
    if (typeof size !== 'number') {
      throw new TypeError('Size must be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('Location must be a string');
    }

    // Store attributes with underscores
    this._size = size;
    this._location = location;
  }

  // Override valueOf to return size when cast to a number
  valueOf() {
    return this._size;
  }

  // Override toString to return location when cast to a string
  toString() {
    return this._location;
  }
}
