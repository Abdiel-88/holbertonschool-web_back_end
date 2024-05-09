// 2-main.js

import getNeighborhoodsList from './2-arrow.js';

// Create a new instance of the class and add a neighborhood
const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res); // Expected output: ['SOMA', 'Union Square', 'Noe Valley']
