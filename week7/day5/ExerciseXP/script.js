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
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

console.log(stock);
currentStock = {...stock};

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

const shoppingList = {
    "banana": 3,
    "orange": 3,
    "apple": 3
}

function myBill() {
    let total = 0;

    for (let item in shoppingList) {
        let quantity = shoppingList[item];

        if (item in stock && stock[item] >= quantity && quantity > 0) {
            total += prices[item] * quantity;
            currentStock[item] -= quantity;
        }
    }
    return total;
}

console.log(`The total bill is: $${myBill()}`);
console.log(currentStock);


// Exercise 3 : What’s in my wallet ?



