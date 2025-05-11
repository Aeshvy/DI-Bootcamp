// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).

const solarSystem = [
  { name: "Mercury", moons: 0, color: "#a9a9a9" },
  { name: "Venus", moons: 0, color: "#ffcc00" },
  { name: "Earth", moons: 1, color: "#0077be" },
  { name: "Mars", moons: 2, color: "#b22222" },
  { name: "Jupiter", moons: 79, color: "#f5deb3" },
  { name: "Saturn", moons: 82, color: "#d2b48c" },
  { name: "Uranus", moons: 27, color: "#66cdaa" },
  { name: "Neptune", moons: 14, color: "#4169e1" },
];

const section = document.querySelector(".listPlanets");

for (let i = 0; i < solarSystem.length; i++) {
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = solarSystem[i].color;
  planetDiv.innerHTML = `${solarSystem[i].name}<br>Moons: ${solarSystem[i].moons}`;

  section.appendChild(planetDiv);

  let left = 150;
  for (let j = 0; j < solarSystem[i].moons; j++) {
    const moonDiv = document.createElement("div");
    moonDiv.classList.add("moon");
    moonDiv.style.position = "absolute";
    moonDiv.style.left = left + "px";
    left += 60;
    planetDiv.appendChild(moonDiv);
  }
}
