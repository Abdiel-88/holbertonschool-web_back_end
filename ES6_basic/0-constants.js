// Use const here because 'task' is not reassigned.
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // This function is fine as it is. It returns a string and does not involve variable reassignment or declaration.
  export function getLast() {
    return ' is okay';
  }
  
  // Use let here because 'combination' is reassigned.
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast(); // Reassigning 'combination'
  
    return combination;
  }
  