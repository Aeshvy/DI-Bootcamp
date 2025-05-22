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

// const totalCost = hotelCost();
// console.log(`The total cost is: ${totalCost}`);

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planeRideCost() {
  while (true) {
    let destination = prompt("Please enter destination: ");

    if (destination !== "" && isNaN(destination)) {
      let chosenDestination = destination.toLowerCase();

      if (chosenDestination === "london") {
        return 183;
      } else if (chosenDestination === "paris") {
        return 220;
      } else {
        return 300;
      }
    } else {
      alert("Please enter a valid destination");
    }
  }
}

// const totalRideCost = planeRideCost();
// console.log(`The cost for this destination is: ${totalRideCost}`);

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

function rentalCarCost() {
  const carDailyRate = 40;
  let numberOfDays;

  while (true) {
    let userInput = prompt("How many days would you like to rent the car? ");
    numberOfDays = parseInt(userInput);

    if (numberOfDays !== "" && !isNaN(numberOfDays) && numberOfDays > 0) {
      break;
    } else {
      alert("Invalid input. Please try again.");
    }
  }

  let carTotalCost = numberOfDays * carDailyRate;
  if (numberOfDays > 10) {
    const discount = carTotalCost * 0.05;
    carTotalCost -= discount;
    alert("You got a 5% discount!");
  } else {
    alert("You are not eligible for a discount.");
  }
  return carTotalCost;
}

// const carTotalCost = rentalCarCost();
// console.log(`The total car rental cost is ${carTotalCost.toFixed(2)}`);

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

function totalVacationCost() {
  const hotelPrice = hotelCost();
  const planePrice = planeRideCost();
  const carPrice = rentalCarCost();

  const vacationCost = hotelPrice + planePrice + carPrice;
  console.log(`Total vacation cost is: ${vacationCost.toFixed(2)}`);
}

// totalVacationCost();
