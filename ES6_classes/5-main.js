// 5-main.js
import Building from './5-building.js';

// Instantiate the Building class directly
const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

// Attempt to create an instance of TestBuilding without overriding the method
try {
    new TestBuilding(200);
} catch (err) {
    console.log(err.message);
}
