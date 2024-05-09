// 12-main.js

import createEmployeesObject from './11-createEmployeesObject.js';
import createReportObject from './12-createReportObject.js';

// Combine multiple departments into one employees object
const employees = {
  ...createEmployeesObject('engineering', ['Bob', 'Jane']),
  ...createEmployeesObject('marketing', ['Sylvie']),
};

// Create a report object based on this employees object
const report = createReportObject(employees);

console.log(report.allEmployees);
console.log(report.getNumberOfDepartments());
