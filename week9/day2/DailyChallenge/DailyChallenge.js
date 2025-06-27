let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

// 1. Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
const displayGroceries = () => {
  groceries.fruits.forEach((fruit) => console.log(fruit));
};

// 2. Create another arrow function named cloneGroceries.
const cloneGroceries = () => {};

// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
const user = client;

// Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?
client = "Betty"; // No, because user is a copy of the value of client, not a reference.

// In the function, create a variable named shopping that is equal to the groceries variable.
let shopping = groceries;

// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
shopping.totalPrice = "35$"; // Yes, because shopping is a reference to the same object as groceries.

// Change the value of the paid key to false. Will we also see this modification in the shopping object ? Why ?
shopping.other.paid = false; // Yes, because shopping.other is a reference to the same object as groceries.other.

// Invoke the cloneGroceries function.
cloneGroceries();
