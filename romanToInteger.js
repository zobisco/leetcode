/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const romanDict = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    if (romanDict[s[i]] < romanDict[s[i + 1]]) {
      sum -= romanDict[s[i]];
    } else {
      sum += romanDict[s[i]];
    }
  }
  return sum;
};

// Test cases:
const romanDict = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
console.log(romanToInt("III") === 3); // 3
console.log(romanToInt("IV") === 4); // 4
console.log(romanToInt("IX") === 9); // 9
console.log(romanToInt("LVIII") === 58); // 58
console.log(romanToInt("DCXXI") === 621); // expected 621
console.log(romanToInt("MCMXCIV") === 1994); // 1994
console.log(romanToInt("MCMXCIX") === 1999); // expected 1999
console.log(romanToInt("MMCDXXV") === 2425); // expected 2425
console.log(romanToInt("MMMCDLXXXVII") === 3487); // 3487

// EOF
