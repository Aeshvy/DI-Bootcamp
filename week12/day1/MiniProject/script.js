let infoBox = document.getElementById("character-info");
let loadingMsg = document.getElementById("loading");
let errorMsg = document.getElementById("error-message");
let findButton = document.getElementById("find-button");

function show(element) {
  element.style.display = "block";
}

function hide(element) {
  element.style.display = "none";
}

// Display character info
function displayCharacter(character, homeWorld) {
  infoBox.innerHTML = `
        <h2>${character.name}</h2>
        <p>Height: ${character.height} cm</p>
        <p>Gender: ${character.gender} </p>
        <p>Birth Year: ${character.birth_year}</p>
        <p>Homeworld: ${homeWorld}</p>
        `;
}

// Fetch random character from API
function getRandomCharacter() {
  const randomId = Math.floor(Math.random() * 83) + 1;

  show(loadingMsg);
  hide(infoBox);
  hide(errorMsg);

  fetch(`https://www.swapi.tech/api/people/${randomId}`)
    .then((response) => {
      if (!response.ok) throw new Error("Character not found");
      return response.json();
    })
    .then((data) => {
      const character = data.result.properties;

      // Now fetch the homeworld
      return fetch(character.homeworld)
        .then((response) => {
          if (!response.ok) throw new Error("Homeworld fetch failed");
          return response.json();
        })
        .then((homeData) => {
          const homeWorld = homeData.result.properties.name;
          displayCharacter(character, homeWorld);
          hide(loadingMsg);
          show(infoBox);
        });
    })
    .catch((error) => {
      console.error("Error fetching character:", error);
      hide(loadingMsg);
      show(errorMsg);
    });
}

// Find button click event
findButton.addEventListener("click", getRandomCharacter);
