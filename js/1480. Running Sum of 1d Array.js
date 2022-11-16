/**
 * @param {number[]} nums
 * @return {number[]}
 */

nums = [1, 2, 3, 4];

// ** Faster speed **
var runningSum = function (nums) {
  let total = 0;
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    total += nums[i];
    result[i] = total;
  }
  return result;
};

// ** Less memory **
// var runningSum = function (nums) {
//   let total = 0;
//   let result = [];
//   for (let i in nums) {
//     total += nums[i];
//     result[i] = total;
//   }
//   return result;
// };

console.log(runningSum(nums));
