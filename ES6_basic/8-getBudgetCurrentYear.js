// 8-getBudgetCurrentYear.js

function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  // Using computed property names
  const currentYear = getCurrentYear();
  const budget = {
    [`income-${currentYear}`]: income,
    [`gdp-${currentYear}`]: gdp,
    [`capita-${currentYear}`]: capita,
  };

  return budget;
}
