// 10-loops.js

export default function appendToEachArrayValue(array, appendString) {
    // Create a new array to avoid modifying the original array directly
    let updatedArray = [];
    
    // Using the 'for...of' loop to iterate through each value directly
    for (const value of array) {
      updatedArray.push(appendString + value);
    }
    
    return updatedArray;
  }
  