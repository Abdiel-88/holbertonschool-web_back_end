// 6-sky_high.js
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Pass sqft to the parent class
    super(sqft);

    // Ensure floors is a number
    if (typeof floors !== 'number') {
      throw new TypeError('Number of floors must be a number');
    }

    this._floors = floors;
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Override evacuationWarningMessage to include the number of floors
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
