// Exercise 1 : Checking the BMI

// Hint:
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// Create two objects, each object should hold a person’s details. Here are the details:
// FullName
// Mass
// Height

// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

// Outside of the objects, create a JS function that compares the BMI of both objects.

// Display the name of the person who has the largest BMI.
const personOne = {
  FullName: "John White",
  Mass: 80,
  Height: 1.8,
  calculateBMI: function () {
    this.bmi = this.Mass / (this.Height * this.Height);
    return this.bmi;
  },
};

const personTwo = {
  FullName: "May Anderssen",
  Mass: 65,
  Height: 1.5,
  calculateBMI: function () {
    this.bmi = this.Mass / (this.Height * this.Height);
    return this.bmi;
  },
};

function compareBMI(personA, personB) {
  const bmiA = personA.calculateBMI();
  const bmiB = personB.calculateBMI();

  if (bmiA > bmiB) {
    console.log(
      `${personA.FullName} has a higher BMI ${bmiA.toFixed(2)} than ${personB.FullName} BMI ${bmiB.toFixed(2)}`
    );
  } else {
    console.log(
      `${personB.FullName} has a higher BMI ${bmiB.toFixed(2)} than ${personA.FullName} BMI ${bmiA.toFixed(2)}}`
    );
  }
}

console.log(compareBMI(personOne, personTwo));
