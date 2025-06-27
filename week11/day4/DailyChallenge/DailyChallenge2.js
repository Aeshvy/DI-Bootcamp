const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`;

// Create three functions. The two first functions should return a promise..

// The first function is named toJs():
// this function converts the morse json string provided above to a morse javascript object.
// if the morse javascript object is empty, throw an error (use reject)
// else return the morse javascript object (use resolve)

function toJs() {
  return new Promise((resolve, reject) => {
    try {
      const morseObj = JSON.parse(morse);
      if (Object.keys(morseObj).length === 0) {
        reject("Morse object is empty.");
      } else {
        resolve(morseObj);
      }
    } catch (error) {
      reject("Error parsing Morse JSON string.");
    }
  });
}

// The second function called toMorse(morseJS), takes one argument: the new morse javascript object.

// This function asks the user for a word or a sentence.
// if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
// else return an array with the morse translation of the user’s word.

function toMorse(morseJS) {
  return new Promise((resolve, reject) => {
    const userInput = prompt(
      "Enter a word or sentence to translate to Morse code:"
    );
    const morseArr = [];

    for (let char of userInput.toLowerCase()) {
      if (morseJS[char]) {
        morseArr.push(morseJS[char]);
      } else {
        reject(`Character "${char}" not found in Morse dictionary.`);
        return; // Stop further execution
      }
    }

    resolve(morseArr);
  });
}

// The third function called joinWords(morseTranslation), takes one argument: the morse translation array

// this function joins the morse translation by using line break and display it on the page (ie. On the DOM)

function joinWords(morseTranslation) {
  return new Promise((resolve, reject) => {
    if (!morseTranslation.length) {
      reject("Array is empty!");
      return;
    }

    const morseString = morseTranslation.join("<br>");
    const outputDiv = document.getElementById("output");

    if (outputDiv) {
      outputDiv.innerHTML = morseString;
      resolve("Morse translation displayed successfully.");
    } else {
      reject("Output div not found.");
    }
  });
}

// Chain the three functions:
toJs()
  .then((morseJS) => {
    return toMorse(morseJS);
  })
  .then((morseTranslation) => {
    return joinWords(morseTranslation);
  })
  .then((message) => {
    console.log(message);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
