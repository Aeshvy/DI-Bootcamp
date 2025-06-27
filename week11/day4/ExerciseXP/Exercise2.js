// Create a promise that resolves itself in 4 seconds and returns a “success” string.

let promise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("success");
  }, 4000);
});