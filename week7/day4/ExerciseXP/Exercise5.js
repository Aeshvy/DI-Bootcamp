// Create an object called family with a few key value pairs.
const family = {
  father: "John",
  mother: "Andrea",
  son: "Alex",
  daughter: "Lara",
};

// Using a for in loop, console.log the keys of the object.
for (const role in family) {
  console.log(role);
}

// Using a for in loop, console.log the values of the object.
for (const name in family) {
  console.log(family[name]);
}
