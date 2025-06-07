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

function winBattle() {
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
const isString = (value) => typeof value === "string";
console.log(isString("hello"));

// 🌟 Exercise 4 : Find the sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
const sum = (a, b) => a + b;
console.log(sum(5, 10));

// 🌟 Exercise 5 : Kg and grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)
// First, use function declaration and invoke it.
function KilosToGrams(kg) {
  return kg * 1000;
}
console.log(KilosToGrams(5));

// Then, use function expression and invoke it.
const kilosToGrams = function (kg) {
  return kg * 1000;
};
console.log(kilosToGrams(5));

// Write in a one line comment, the difference between function declaration and function expression.
// functions are hoisted (moved) to the top of their scope, while expressions are not.

// Finally, use a one line arrow function and invoke it.
const kilosToGrams2 = (kg) => kg * 1000;
console.log(kilosToGrams2(5));

// 🌟 Exercise 6 : Fortune teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."
(function (children, partner, location, job) {
  const message = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
  document.body.innerHTML = `<p>${message}</p>`;
})(3, "Alice", "New York", "Software Engineer");

// 🌟 Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.
// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.
(function (username) {
  const navbar = document.querySelector(".navbar");
  const userDiv = document.createElement("div");
  userDiv.innerHTML = `<p>Welcome, ${username}!</p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAd5avdba8EiOZH8lmV3XshrXx7dKRZvhx-A&s">`;
  navbar.appendChild(userDiv);
})("John Doe");

// 🌟 Exercise 8 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.
// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.
function makeJuice(size) {
  function addIngredients(ingredient1, ingredient2, ingredient3) {
    const message = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}.`;

    // Display it on the DOM
    const output = document.createElement("p");
    output.textContent = message;
    document.body.appendChild(output);
  }

  addIngredients("apple", "carrot", "ginger");
}

makeJuice("large");

// Part II:
// In the makeJuice function, create an empty array named ingredients.

// The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

// Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.
function makeJuice(size) {
  const ingredients = [];

  function addIngredients(ingredient1, ingredient2, ingredient3) {
    ingredients.push(ingredient1, ingredient2, ingredient3);
  }

  function displayJuice() {
    const message = `The client wants a ${size} juice, containing ${ingredients.join(
      ", "
    )}.`;

    const output = document.createElement("p");
    output.textContent = message;
    document.body.appendChild(output);
  }

  addIngredients("apple", "carrot", "ginger");
  addIngredients("banana", "lemon", "mint");

  displayJuice();
}

makeJuice("medium");
