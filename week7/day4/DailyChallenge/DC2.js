// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.

// First loop:
for (let i = 1; i <= 6; i++) {
  console.log("* ".repeat(i));
}

// Second loop:
for (let j = 0; j <= 6; j++) {
  let symbols = "";
  for (let k = 1; k <= j; k++) {
    symbols += "* ";
  }
  console.log(symbols);
}
