// Exercise 1 : Divisible by three
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



// Exercise 2 : Attendance
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

// Prompt the student for their name.
prompt(guestList[0])

// If the name is in the object, console.log the name of the student and the country they come from.
// For example: "Hi! I'm [name], and I'm from [country]."
// Hint: You don’t need to use a for loop, just look up the statement if ... in

// If the name is not in the object, console.log: "Hi! I'm a guest."
