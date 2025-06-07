// 🌟 Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.

// #1
function funcOne() {
  let a = 5;
  if (a > 1) {
    a = 3;
  }
  alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne();
// #1.2 What will happen if the variable is declared
// with const instead of let ?

// if 'a' is declared with const, it will throw an error because const variables cannot be reassigned.

//#2
let a = 0;
function funcTwo() {
  a = 5;
}

function funcThree() {
  alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree(); // a = 0
funcTwo(); // a = 5
funcThree(); // a = 5
// #2.2 What will happen if the variable is declared
// with const instead of let ?

// if 'a' is declared with const, it will throw an error because const variables cannot be reassigned.

//#3
function funcFour() {
  window.a = "hello";
}

function funcFive() {
  alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour();
funcFive(); // a = "hello"

//#4
let a = 1;
function funcSix() {
  let a = "test"; // scope of 'a' is local to funcSix
  alert(`inside the funcSix function ${a}`); // a = "test"
}

// #4.1 - run in the console:
funcSix();
// #4.2 What will happen if the variable is declared
// with const instead of let ?
// If `let a = "test"` is replaced by `const a = "test"`. It will work because it is not being reassigned, just declared in a different scope.

//#5
let a = 2;
if (true) {
  let a = 5;
  alert(`in the if block ${a}`); // a = 5
}
alert(`outside of the if block ${a}`); // a = 2

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared
// with const instead of let ?

// 🌟 Exercise 2 : Ternary operator
// Instructions
// Using the code below:

function winBattle(){
    return true;
}

// Transform the winBattle() function to an arrow function.
const winBattle = () => true;
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
const experiencePoints = winBattle() ? 10 : 1;
// Console.log the experiencePoints variable.
console.log(experiencePoints);

// 🌟 Exercise 3 : Is it a string ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output
const isString = (value) => typeof value === 'string';
console.log(isString("hello")); 

// 🌟 Exercise 4 : Find the sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
const sum = (a, b) => a + b;
console.log(sum(5, 10));


