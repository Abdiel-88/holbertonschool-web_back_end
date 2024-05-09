// 1-block-scoped.js

export default function taskBlock(trueOrFalse) {
    // Use let for block-scoped variables
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      // Variables declared with let are scoped to the if block
      let task = true;
      let task2 = false;
      console.log(`Inside block: [${task}, ${task2}]`); // For debugging (optional)
    }
  
    // Outer task and task2 will remain unchanged by the inner block
    return [task, task2];
  }
  