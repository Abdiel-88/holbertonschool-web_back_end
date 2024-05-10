// 3-currency.js
export default class Currency {
  constructor(code, name) {
    // Ensure proper types for each attribute
    this.code = code;
    this.name = name;
  }

  // Getters
  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  // Setters
  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  // Method that returns 'name (code)'
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
