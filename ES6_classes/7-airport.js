// 7-airport.js
export default class Airport {
    constructor(name, code) {
        // Verify data types
        if (typeof name !== 'string') {
            throw new TypeError('Name must be a string');
        }
        if (typeof code !== 'string') {
            throw new TypeError('Code must be a string');
        }

        // Store attributes with underscores
        this._name = name;
        this._code = code;
    }

    // Override toString method to return the airport code
    toString() {
        return `[object ${this._code}]`;
    }
}
