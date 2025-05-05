// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let userInput = prompt("Input a number: ");
if (isNaN(userInput)) {
  console.log("You entered a string!");
} else {
  console.log("You entered an integer!");
}

while (userInput < 10) {
  userInput = prompt("Input a number: ");
  console.log("The number is less than 10!");
  userInput = Number(userInput);
}
console.log("The number is greater than 10!");
