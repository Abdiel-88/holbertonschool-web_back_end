// 4-pricing.js
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    // Ensure the amount is a number and currency is an instance of Currency
    this.amount = amount;
    this.currency = currency;
  }

  // Getters
  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  // Setters
  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of the Currency class');
    }
    this._currency = newCurrency;
  }

  // Method to display the full price
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert the price using a conversion rate
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
