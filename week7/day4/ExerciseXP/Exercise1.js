const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review about arrays
// Write code to remove “Greg” from the people array.
people.splice(0, 1);
console.log(people);

// Write code to replace “James” to “Jason”.
people[2] = "Jason";
console.log(people);

// Write code to add your name to the end of the people array.
people.push("Alex");
console.log(people);

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
console.log(people.indexOf("Mary"));

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
console.log(people.slice(1, 3));

// Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo"));

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
last = people[people.length - 1];
console.log(last);

// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.
for (let name of people) {
  console.log(name);
}

// Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// Hint: take a look at the break statement in the lesson.
for (let name of people) {
  console.log(name);
  if (name == "Devon") break;
}
console.log("The loop has reached Devon..");
