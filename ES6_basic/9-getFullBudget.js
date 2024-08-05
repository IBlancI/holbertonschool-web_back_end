import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) { // Méthode ES6
      return `$${income}`;
    },
    getIncomeInEuros(income) { // Méthode ES6
      return `${income} euros`;
    },
  };

  return fullBudget;
}
