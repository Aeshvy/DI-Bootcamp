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
  let nights;

  while (true) {
    nights = prompt("How many nights? ");
    if (nights !== null) {
      nights = nights.trim();
    }
  }
}