const _ = require('lodash');
const { add, multiply } = require('./math');

console.log("Sum:", add(5, 7));
console.log("Product:", multiply(3, 4));

const numbers = [1, 2, 3, 4, 5];
console.log("Max:", _.max(numbers));