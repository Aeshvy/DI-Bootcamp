// 🌟 Exercise 1 : Change the article

// Using a DOM property, retrieve the h1 and console.log it.
const h1Element = document.querySelector("h1");
console.log(h1Element);
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
    article.style.fontWeight = 'bold';
});
