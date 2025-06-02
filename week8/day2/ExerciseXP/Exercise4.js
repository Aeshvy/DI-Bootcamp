function calculateSphereVolume(r) {
  return ((4 / 3) * Math.PI * r ** 3).toFixed(2);
}

window.onload = () => {
  document.getElementById("MyForm").onsubmit = (e) => {
    e.preventDefault();
    const r = parseFloat(document.getElementById("radius").value);
    if (r > 0) {
      const v = calculateSphereVolume(r);
      document.getElementById("volume").value = v;
      console.log(`Volume of the sphere with radius ${r} is: ${v}`);
    } else {
      alert("Please enter a valid positive number for radius.");
    }
  };
};
