// 1-main.js
import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));  // Expect to see [false, true]
console.log(taskBlock(false)); // Expect to see [false, true]
