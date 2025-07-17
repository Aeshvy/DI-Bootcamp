// In app.js, import the functions from the fileManager.js module.
import { readFile, writeFile } from "./fileManager.js";

// Use the imported functions to read the content of the “Hello World.txt” text file and then write to the “Bye World.txt” with the content “Writing to the file”.

const helloFilePath = "./Hello World.txt";
const byeFilePath = "./Bye World.txt";  

// Read the content of "Hello World.txt"
writeFile(byeFilePath, "Writing to the file", (err) => {
  if (err) {
    console.error("Error writing to Bye World.txt:", err);
  } else {
    console.log("Successfully wrote to Bye World.txt");
  }
});