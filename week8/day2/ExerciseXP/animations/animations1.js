// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
// function helloWorld () {
setTimeout(function () {
  alert("Hello World");
}, 2000);

// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
setTimeout(function () {
  const paragraph = document.createElement("p");
  paragraph.textContent = "Hello World";
  document.getElementById("container").appendChild(paragraph);
}, 2000);

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.
let count = 0;
const container = document.getElementById("container");

const intervalId = setInterval(function () {
  if (count >= 5) {
    clearInterval(intervalId);
    return;
  }
  const paragraph = document.createElement("p");
  paragraph.textContent = "Hello World";
  container.appendChild(paragraph);
  count++;
}, 2000);

document.getElementById("clear").addEventListener("click", function () {
  clearInterval(intervalId);
});
