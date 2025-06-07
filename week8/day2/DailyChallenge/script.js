document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("libform");
  const storySpan = document.getElementById("story");

  const inputs = ["noun", "adjective", "person", "verb", "place"];

  const templates = [
    (w) =>
      `${w.person} went to ${w.place} with a ${w.adjective} ${w.noun} and decided to ${w.verb} all day.`,
    (w) =>
      `In ${w.place} far away, ${w.person} found a ${w.adjective} ${w.noun} and tried to ${w.verb} it.`,
    (w) =>
      `Why did ${w.person} bring a ${w.adjective} ${w.noun} to ${w.place}? To ${w.verb}, of course!`,
  ];

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const values = {};
    for (let id of inputs) {
      const val = document.getElementById(id).value.trim();
      if (!val) return alert(`Please fill out the ${id} field.`);
      values[id] = val;
    }

    const randomTemplate =
      templates[Math.floor(Math.random() * templates.length)];
    storySpan.textContent = randomTemplate(values);
  });
});
