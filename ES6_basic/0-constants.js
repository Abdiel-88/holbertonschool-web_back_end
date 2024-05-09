// 0-constants.js

// Use 'const' for variables that won't change
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // Function to return a fixed string
  export function getLast() {
    return ' is okay';
  }
  
  // Use 'let' for variables that might change
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();
  
    return combination;
  }
  