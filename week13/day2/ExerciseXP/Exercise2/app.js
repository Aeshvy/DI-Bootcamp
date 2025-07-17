// In app.js, import the array of person objects from the data.js module.
import people from "./data.js";

// Write a function that calculates and prints the average age of all the persons in the array.
function findAverageAge() {
  const totalAge = people.reduce((sum, person) => sum + person.age, 0);
  return totalAge / people.length;
}

// Use the imported array and the average age function in app.js.
console.log("Average Age:", findAverageAge());

// Run app.js and confirm that the average age is correctly calculated and displayed.
// node app.js
