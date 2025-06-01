// 🌟 Exercise 1 : Change the article

// Using a DOM property, retrieve the h1 and console.log it.
const h1Element = document.querySelector("h1");
console.log("h1 element: ", h1Element);
// Using DOM methods, remove the last paragraph in the <article> tag.
const article = document.querySelector("article");
const lastPar = article.querySelector("p:last-of-type");
article.removeChild(lastPar);
// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
const h2Element = document.querySelector("h2");
h2Element.addEventListener("click", function () {
  h2Element.style.backgroundColor = "red";
});
// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
const h3Hidden = document.querySelector("h3");
h3Hidden.addEventListener("click", function () {
  h3Hidden.style.display = "none";
});
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
const boldBtn = document.getElementById("boldButton");
boldBtn.addEventListener("click", function () {
  article.style.fontWeight = "bold";
});

// 🌟 Exercise 2 : Work with forms

// Retrieve the form and console.log it.
form = document.querySelector("form");
console.log("form element: ", form);
// Retrieve the inputs by their id and console.log them.
const firstNameInput = document.getElementById("fname");
const lastNameInput = document.getElementById("lname");
console.log("First Name Input (by ID):", firstNameInput);
console.log("Last Name Input (by ID):", lastNameInput);
// Retrieve the inputs by their name attribute and console.log them.
const firstNameByName = document.getElementsByName("firstname")[0];
const lastNameByName = document.getElementsByName("lastname")[0];
console.log("First Name Input (by Name):", firstNameByName);
console.log("Last Name Input (by Name):", lastNameByName);
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
const usersAnswerList = document.querySelector(".usersAnswer");
form.addEventListener("submit", function (event) {
  event.preventDefault();

  const firstName = firstNameInput.value.trim();
  const lastName = lastNameInput.value.trim();

  if (firstName === "" || lastName === "") {
    alert("Please fill in both first and last names.");
    return;
  }

  const li1 = document.createElement("li");
  li1.textContent = `First name: ${firstName}`;
  usersAnswerList.appendChild(li1);

  const li2 = document.createElement("li");
  li2.textContent = `Last name: ${lastName}`;
  usersAnswerList.appendChild(li2);
});
