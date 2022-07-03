/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  if (nums.length === 2) {
    return [0, 1];
  }
  visitedNumbers = new Map();
  for (let num of nums) {
    let desiredNum = target - num;
    if (visitedNumbers.has(desiredNum)) {
      let indexOfDesiredNum = nums.indexOf(desiredNum);
      let indexOfNum = nums.lastIndexOf(num);
      return [indexOfDesiredNum, indexOfNum];
    } else {
      visitedNumbers.set(num);
    }
  }
};

// time complexity is O(n)
// worst case scenario: looping through 10k numbers

console.log(twoSum([2, 7, 11, 15], 9)); // expected [0, 1]
console.log(twoSum([3, 2, 4], 6)); // expected [1, 2]
console.log(twoSum([3, 3], 6)); // expected [0, 1]
console.log(twoSum([3, 2, 3], 6)); // expected [0, 2]
console.log(twoSum([3, 3, 2], 6)); // expected [0, 1]
console.log(twoSum([2, 3, 3], 6)); // expected [1, 2]

// EOF
