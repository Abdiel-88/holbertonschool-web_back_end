// 12-createReportObject.js

export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    // ES6 method property syntax
    getNumberOfDepartments() {
      // The number of keys in employeesList represents the departments
      return Object.keys(employeesList).length;
    },
  };
}
