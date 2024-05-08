export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    task = true;// Affecting the outer scope directly
    task2 = false;// Affecting the outer scope directly
  }

  console.log(`Final values: task = ${task}, task2 = ${task2}`);
  return [task, task2];
}
