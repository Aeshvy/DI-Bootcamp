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
      `${personA.FullName} has a higher BMI of: ${bmiA.toFixed(2)} than ${
        personB.FullName
      } BMI of: ${bmiB.toFixed(2)}`
    );
  } else {
    console.log(
      `${personB.FullName} has a higher BMI of: ${bmiB.toFixed(2)} than ${
        personA.FullName
      } BMI of: ${bmiA.toFixed(2)}}`
    );
  }
}

console.log(compareBMI(personOne, personTwo));

// Exercise 2 : Grade Average

// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

// Create a function called findAvg(gradesList) that takes an argument called gradesList.

// Your function must calculate and console.log the average.

// If the average is above 65 let the user know they passed

// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.
const gradesList = [65, 55, 70, 95, 35];

function findAvg(gradesList) {
  let total = 0;
  for (let i = 0; i < gradesList.length; i++) {
    total += gradesList[i];
  }
  let average = total / gradesList.length;
  return average;
}
const average = findAvg(gradesList);

if (average < 65) {
  console.log(`Your average is ${average}. You must repeat the course.`)
}