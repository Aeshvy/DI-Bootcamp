document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("myForm");
  const output = document.getElementById("output");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Get values
    const name = document.getElementById("name").value;
    const lastName = document.getElementById("lastName").value;

    // JSON object
    const formData = {
      name: name,
      lastName: lastName,
    };

    // Convert to JSON string
    output.textContent = JSON.stringify(formData, null, 2);
  });
});
