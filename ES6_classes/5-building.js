// 5-building.js
export default class Building {
  constructor(sqft) {
    // Ensure the square footage is a number
    if (typeof sqft !== 'number') {
      throw new TypeError('Square footage must be a number');
    }
    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Abstract method to be overridden by subclasses
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
