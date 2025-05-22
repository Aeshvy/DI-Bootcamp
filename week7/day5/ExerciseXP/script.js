// Exercise 1 : Find the numbers divisible by 23

// Create a function call displayNumbersDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

function displayNumbersDivisible() {
  const divisibleNumbers = [];

  console.log("All numbers divisible by 23:");

  for (let i = 0; i <= 500; i++) {
    if (i % 23 === 0) {
      console.log(i);
      divisibleNumbers.push(i);
    }
  }
  return divisibleNumbers;
}

const numbers = displayNumbersDivisible();

let sum = 0;
for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}

console.log("Total sum of numbers:", sum);

// Exercise 2 : Shopping List

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// Bonus: If the item is in stock, decrease the item’s stock by 1

const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};

const shoppingList = {
  banana: 1,
  orange: 1,
  apple: 1,
};

function myBill() {
  let total = 0;

  for (let item in shoppingList) {
    let quantity = shoppingList[item];

    if (item in stock && stock[item] >= quantity && quantity > 0) {
      total += prices[item] * quantity;
      stock[item] -= quantity;
    }
  }
  return total;
}

console.log(`The total bill is: $${myBill()}`);

// Exercise 3 : What’s in my wallet ?

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

function changeEnough(itemPrice, amountOfChange) {
  const values = {
    quarter: 0.25,
    dime: 0.1,
    nickel: 0.05,
    penny: 0.01,
  };

  const coins = ["quarter", "dime", "nickel", "penny"];

  let changeEnough = 0;
  for (let i = 0; i < amountOfChange.length; i++) {
    changeEnough += amountOfChange[i] * values[coins[i]];
  }
  return changeEnough >= itemPrice;
}

console.log(`Sufficient amout: ${changeEnough(4.25, [25, 20, 5, 0])}`);

// Exercise 4 : Vacations Costs

// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

function hotelCost() {
  const pricePerNight = 140;

  while (true) {
    let nights = prompt("How many nights? ");

    if (nights !== "" && !isNaN(nights) && Number(nights) > 0) {
      return Number(nights) * pricePerNight;
    } else {
      alert("Invalid input! Please try again.");
    }
  }
}

const totalCost = hotelCost();
console.log(`The total cost is: ${totalCost}`);

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planetRideCost() {
  while (true) {
   let destination = prompt("Please enter destination: ");
   
   if (destination !== "" && isNaN(destination)) {
    let chosenDestination = destination.toLowerCase();

    if (chosenDestination === 'london') {
      return 183;
    } else if (chosenDestination === 'paris') {
      return 220;
    } else {
      return 300;
    }
    } else {
      alert("Please enter a valid destination");
    }
  }
}

const totalRideCost = planetRideCost();
console.log(`The cost for this destination is: ${totalRideCost}`);

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

function rentalCarCost() {
  const carDailyRate = 40;

  while (true) {
    let carRentalDuration = prompt("How many days would you like to rent the car? ");
    if (carRentalDuration !== '' && isNaN(carRentalDuration));

    
    
  }
}

// FUNCTION rentalCarCost()
//     HINT: This function will calculate and return the total price for a car rental
//     based on user input (number of days), with input validation and a discount rule.

//     ----------------------------------------------------------
//     Step 1: Set the constant rental price per day
//     ----------------------------------------------------------
//     DECLARE dailyRate = 40
//     HINT: Each day of rental costs $40

//     ----------------------------------------------------------
//     Step 2: Declare variable to store number of days
//     ----------------------------------------------------------
//     DECLARE numberOfDays

//     ----------------------------------------------------------
//     Step 3: Start a loop to ask the user for input until it’s valid
//     ----------------------------------------------------------
//     LOOP until numberOfDays is a valid number AND greater than 0

//         DISPLAY prompt asking:
//             "How many days would you like to rent the car?"

//         STORE the user's input in variable userInput

//         TRY to CONVERT userInput to a number (e.g., using parseInt)

//         IF conversion is successful AND the number is greater than 0 THEN
//             SET numberOfDays = converted number
//             BREAK the loop
//         ELSE
//             DISPLAY message:
//                 "Invalid input. Please enter a positive whole number of days."

//     END LOOP

//     ----------------------------------------------------------
//     Step 4: Calculate the base cost
//     ----------------------------------------------------------
//     SET totalCost = numberOfDays * dailyRate

//     ----------------------------------------------------------
//     Step 5: Check if the user qualifies for a 5% discount
//     ----------------------------------------------------------
//     IF numberOfDays > 10 THEN
//         CALCULATE discountAmount = totalCost * 0.05
//         SUBTRACT discountAmount from totalCost
//         HINT: Apply the 5% discount

//     END IF

//     ----------------------------------------------------------
//     Step 6: Display and return the result
//     ----------------------------------------------------------
//     DISPLAY message:
//         "The total cost to rent the car for [numberOfDays] days is $" + totalCost

//     RETURN totalCost

// END FUNCTION