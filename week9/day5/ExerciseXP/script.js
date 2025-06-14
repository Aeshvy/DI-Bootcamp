// 🌟 Exercise 1 : Location
// Instructions
// Analyze the code below. What will be the output?
const person = {
  name: "John Doe",
  age: 25,
  location: {
    country: "Canada",
    city: "Vancouver",
    coordinates: [49.2827, -123.1207],
  },
};

const {
  name,
  location: {
    country,
    city,
    coordinates: [lat, lng],
  },
} = person;
console.log(
  `I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`
);
// Output: I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// 🌟 Exercise 2: Display Student Info
// Instructions
function displayStudentInfo(objUser) {
  //destructuring
}

displayStudentInfo({ first: "Elie", last: "Schoppik" });
// Using the code above, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'
function displayStudentInfo(objUser) {
  const { first, last } = objUser;
  return `Your full name is ${first} ${last}`;
}

// 🌟 Exercise 3: User & id
// Instructions
// Using this object:
const users = { user1: 18273, user2: 92833, user3: 90315 };

// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.
const arr = Object.entries(users);
console.log(arr);

// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]
const usersMultiplied = arr.map(([key, value]) => [key, value * 2]);
console.log(usersMultiplied);

// 🌟Exercise 4 : Person class
// Instructions
// Analyze the code below. What will be the output?
class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person("John");
console.log(typeof member);
// Output: object

// 🌟 Exercise 5 : Dog class
// Instructions
// Using the Dog class below:

class Dog {
  constructor(name) {
    this.name = name;
  }
}

// Analyze the options below. Which constructor will successfully extend the Dog class?
// 1
class Labrador extends Dog {
  constructor(name, size) {
    this.size = size;
  }
}

// 2
class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
}

// 3
class Labrador extends Dog {
  constructor(size) {
    super(name);
    this.size = size;
  }
}

// 4
class Labrador extends Dog {
  constructor(name, size) {
    this.name = name;
    this.size = size;
  }
}

// The correct option is 2.

// 🌟 Exercise 6 : Challenges
// Evaluate these (ie True or False)

// [2] === [2] Output:  False
// {} === {} OutputL    False

// What is, for each object below, the value of the property number and why?

const object1 = { number: 5 }; // Output: 5 because it is the initial value assigned to the property number.
const object2 = object1; // Output: 5 because object2 is a reference to object1, so it points to the same object in memory.
const object3 = object2; // Output: 5 because object3 is also a reference to object1, so it points to the same object in memory.
const object4 = { number: 5 }; // Output: 5 because it is a new object with the same property value, but it is not a reference to object1 or object2.

object1.number = 4;
console.log(object2.number); // Output: 4 because object2 is a reference to object1, and changing object1's property affects object2.
console.log(object3.number); // Output: 4 because object3 is also a reference to object1, and changing object1's property affects object3.
console.log(object4.number); // Output: 5 because object4 is a separate object with its own property value, which remains unchanged despite changes to object1, object2, and object3.

// 1. Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin etc …
class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }

  // Method to display animal information
  displayInfo() {
    return `This is a ${this.color} ${this.type} named ${this.name}.`;
  }
}

// 2.  Create a class Mammal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.
class Mammal extends Animal {
  constructor(name, type, color) {
    super(name, type, color);
  }

  sound(animalSound) {
    return `${this.name} is a ${this.color} ${this.type} and it makes a sound: ${animalSound}.`;
  }
}

// 3. Create a farmerCow object that is an instance of the class Mammal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
// For example: Moooo I'm a cow, named Lily and I'm brown and white
const formerCow = new Mammal("Lilly", "cow", "brown and white", "moo");
console.log(
  formerCow.sound("Moooo I'm a cow, named Lilly and I'm brown and white")
);
