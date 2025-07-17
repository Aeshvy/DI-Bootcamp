// In shop.js, require the product objects from the products.js module.
const products = require('./products');

// Create a function that takes a product name as a parameter and searches for the corresponding product object.
function findProductByName(productName) {
  return products.find(product => product.name.toLowerCase() === productName.toLowerCase());
}

// Call this function with different product names and print the details of the products.
console.log(findProductByName("Laptop"));
console.log(findProductByName("Coffee Maker"));
console.log(findProductByName("Running Shoes"));

// Run shop.js and verify that the correct product details are displayed.
// node shop.js