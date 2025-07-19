const express = require("express");
const app = express();
const PORT = 5000;

const { fetchPosts } = require("./data/dataService");

app.get("/", async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log("Data successfully retrieved and sent.");
    res.json(posts);
  } catch (error) {
    res.status(500).json({ message: "Error fetching data" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
