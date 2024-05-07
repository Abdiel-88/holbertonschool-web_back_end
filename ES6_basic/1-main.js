import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));   // Should log: [false, true]
console.log(taskBlock(false));  // Should log: [false, true]
