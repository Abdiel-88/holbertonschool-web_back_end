// 11-createEmployeesObject.js

export default function createEmployeesObject(departmentName, employees) {
  // Use computed property name syntax to set the department name as a key
  return {
    [departmentName]: employees,
  };
}
