/**
 * @param {number[][]} accounts
 * @return {number}
 */

accounts = [
  [1, 5],
  [7, 3],
  [3, 5],
];

var maximumWealth = function (accounts) {
  total = [];
  for (let i in accounts) {
    total[i] = accounts[i].reduce((partialSum, a) => partialSum + a, 0);
  }
  return Math.max(...total);
};

console.log(maximumWealth(accounts));
