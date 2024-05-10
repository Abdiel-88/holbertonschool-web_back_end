import listOfStudents from './9-hoisting.js';

// Output the whole list of students
console.log(listOfStudents);

// Map through the list and print each student's full description
const listPrinted = listOfStudents.map(
  (student) => student.fullStudentDescription,
);

console.log(listPrinted);
