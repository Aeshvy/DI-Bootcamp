const multi = (a, b) => a * b;
const add = (a, b) => a + b;
const sub = (a, b) => a - b;
const div = (a, b) => {
  if (b === 0) throw new Error("Division by zero is not allowed");
  return a / b;
};

console.log(multi(2, 3));
console.log(add(2, 3));
console.log(sub(2, 3));
console.log(div(2, 3));

module.exports = {
  multi,
  add,
  sub,
  div,
};