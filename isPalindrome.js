/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  const palindrome = x.toString().split("").reverse().join("");
  return palindrome === x.toString();
};

// EOF
