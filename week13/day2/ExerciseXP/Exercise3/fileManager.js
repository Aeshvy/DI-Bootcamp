// Inside fileManager.js, define a module that exports functions for reading and writing files.
import fs from "fs";

// Export functions named readFile and writeFile.
// Implement the readFile function to read the content of a specified file using the fs module.
export function readFile(filePath, callback) {
  fs.readFile(filePath, "utf8", (err, data) => {
    if (err) {
      return callback(err);
    }
    callback(null, data);
  });
}

// Implement the writeFile function to write content to a specified file using the fs module.
export function writeFile(filePath, content, callback) {
  fs.writeFile(filePath, content, "utf8", (err) => {
    if (err) {
      return callback(err);
    }
    callback(null);
  });
}
