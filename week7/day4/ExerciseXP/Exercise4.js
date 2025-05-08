// Copy and paste the above object to your Javascript file.

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    Sarah: [3, 990],
    Dan: [4, 1000],
    David: [1, 500],
  },
};

// Console.log the number of floors in the building.
console.log(building.numberOfFloors);

// Console.log how many apartments are on the floors 1 and 3.
console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(
  building.nameOfTenants[1],
  building.numberOfRoomsAndRent[building.nameOfTenants[1]][0]
);

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
let sarahRent = building.numberOfRoomsAndRent[building.nameOfTenants[0]][1];
let danRent = building.numberOfRoomsAndRent[building.nameOfTenants[1]][1];
let davidRent = building.numberOfRoomsAndRent[building.nameOfTenants[2]][1];

if (sarahRent + davidRent > danRent) {
  danRent = 1200;
  console.log(danRent);
}
