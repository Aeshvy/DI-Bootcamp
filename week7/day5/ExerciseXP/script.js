// 🌟 Exercise 1 : Find the numbers divisible by 23

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

// 🌟 Exercise 2 : Shopping List

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

// 🌟 Exercise 3 : What’s in my wallet ?

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

// 🌟 Exercise 4 : Vacations Costs

// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

function hotelCost() {
  const pricePerNight = 140;

  while (true) {
    let nights = prompt("How many nights? ");
    if (nights === null) {
      return null;
    }

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
    if (destination === null) {
      return null;
    }

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
    let cars = prompt("How many days would you like to rent the car? ");
    if (cars === null) {
      return null;
    }
    numberOfDays = parseInt(cars);

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
  if (hotelPrice === null) {
    return; // exit totalVacationCost early
  }
  const planePrice = planeRideCost();
  if (planePrice === null) {
    return;
  }
  const carPrice = rentalCarCost();
  if (carPrice === null) {
    return;
  }

  const vacationCost = hotelPrice + planePrice + carPrice;
  console.log(`Total vacation cost is: ${vacationCost.toFixed(2)}`);
}

totalVacationCost();

// 🌟 Exercise 5 : Users

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the second <li> of the second <ul>.
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

let containerDiv = document.getElementById("container");
console.log(containerDiv);

let allUlElements = document.querySelectorAll(".list");
let firstUl = allUlElements[0];
firstUl.children[1].textContent = "Richard";

let secondUl = allUlElements[1];
secondUl.removeChild(secondUl.children[1]);

allUlElements.forEach((ul) => {
  ul.children[0].textContent = "Alex";
});

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

allUlElements.forEach((ul) => {
  ul.classList.add("student_list");
});

firstUl.classList.add("university", "attendance");
console.log(firstUl);

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.

containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

let hideDan = secondUl.lastElementChild;
hideDan.style.display = "none";

firstUl.children[1].style.border = "5px solid black";

document.body.style.fontSize = "20px";

// 🌟 Exercise 6 : Change the navbar

// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).

let NavDiv = document.getElementById("navBar");

NavDiv.setAttribute("id", "socialNetworkNavigation");

let ul = document.querySelector("#socialNetworkNavigation ul");

let newLi = document.createElement("li");

let logoutText = document.createTextNode("Logout");
newLi.appendChild(logoutText);

ul.appendChild(newLi);

let firstLi = ul.firstElementChild;
let lastLi = ul.lastElementChild;

console.log("First link text:", firstLi.textContent);
console.log("Last link text:", lastLi.textContent);

// 🌟 Exercise 7 : My Book List

// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).

// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.

let allBooks = [
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image:
      "https://m.media-amazon.com/images/I/712cDO7d73L._AC_UF1000,1000_QL80_.jpg",
    alreadyRead: true,
  },
  {
    title: "Harry Potter and the Sorcerer's Stone",
    author: "J.K. Rowling",
    image:
      "https://m.media-amazon.com/images/I/91wKDODkgWL._AC_UF1000,1000_QL80_DpWeblab_.jpg",
    alreadyRead: false,
  },
];

const bookSection = document.querySelector(".listBooks");

allBooks.forEach((book) => {
  let bookDiv = document.createElement("div");
  bookDiv.style.marginBottom = "20px";

  let bookInfo = document.createElement("p");
  bookInfo.textContent = `${book.title} written by ${book.author}`;

  if (book.alreadyRead) {
    bookInfo.style.color = "red";
  }

  let bookImg = document.createElement("img");
  bookImg.src = book.image;
  bookImg.alt = book.title;
  bookImg.style.width = "100px";

  bookDiv.appendChild(bookInfo);
  bookDiv.appendChild(bookImg);

  bookSection.appendChild(bookDiv);
});
