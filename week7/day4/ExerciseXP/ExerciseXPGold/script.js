// Exercise 1 : Divisible by three-----------------------------------
let numbers = [123, 8409, 100053, 333333333, 7];

// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log true or false.
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 3 == 0) {
    console.log(`${numbers[i]}: True`);
  } else {
    console.log(`${numbers[i]}: False`);
  }
}

// Exercise 2 : Attendance------------------------------------------
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina",
};

// Prompt the student for their name.

// If the name is in the object, console.log the name of the student and the country they come from.
// For example: "Hi! I'm [name], and I'm from [country]."
// Hint: You don’t need to use a for loop, just look up the statement if ... in

// If the name is not in the object, console.log: "Hi! I'm a guest."
let name = prompt("What's your name?");

if (guestList[name]) {
  console.log(`Hi, I'm from ${guestList[name]}.`);
} else {
  console.log("Hi, I'm a guest.");
}

// Exercise 3 : Playing with numbers---------------------------------------
let age = [20, 5, 12, 43, 98, 55];

// Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for loops.

// 1. Console.log the sum of all the numbers in the age array.
for (let i = 0; i < age.length; i++) {}

// 2. Console.log the highest age in the array.
