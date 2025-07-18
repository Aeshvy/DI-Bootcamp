// const express = require("express");
// const { emojis } = require("./models/emojis");

// const app = express();
// app.use("/", express.static(__dirname + "/public"));

// const PORT = process.env.PORT || 3001;

// app.listen(PORT, () => {
//   console.log(`run on ${PORT}`);
// });

// const shuffleArray = (array) => {
//   for (let i = array.length - 1; i > 0; i--) {
//     const j = Math.floor(Math.random() * (i + 1));
//     [array[i], array[j]] = [array[j], array[i]];
//   }
//   return array;
// };

// app.get("/emojis", (req, res) => {
//   const randomIndex = Math.floor(Math.random() * emojis.length);
//   const randomEmoji = emojis[randomIndex];
//   const shuffleEmojis = shuffleArray(emojis);
//   res.json(randomEmoji, shuffleEmojis);
// });

// server.js
const express = require("express");
const path = require("path");
const emojis = require("./models/emojis");
console.log("Loaded emojis:", emojis);
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

let leaderboard = [];

function getEmojiQuestion() {
  const correct = emojis[Math.floor(Math.random() * emojis.length)];
  const options = [correct.name];

  while (options.length < 4) {
    const choice = emojis[Math.floor(Math.random() * emojis.length)].name;
    if (!options.includes(choice)) options.push(choice);
  }

  return {
    emoji: correct.emoji,
    correctAnswer: correct.name,
    options: shuffleArray(options),
  };
}

function shuffleArray(arr) {
  return arr.sort(() => Math.random() - 0.5);
}

app.get("/question", (req, res) => {
  const question = getEmojiQuestion();
  if (!question)
    return res.status(500).json({ error: "Emoji data not available" });
  res.json(question);
});

// Handle guess
app.post("/guess", (req, res) => {
  const { answer, correctAnswer, player } = req.body;

  if (!player) {
    return res.status(400).json({ error: "Player name is required" });
  }

  const isCorrect = answer === correctAnswer;

  let existing = leaderboard.find((entry) => entry.name === player);
  if (!existing) {
    existing = { name: player, score: 0 };
    leaderboard.push(existing);
  }

  if (isCorrect) {
    existing.score += 1;
  }

  res.json({ correct: isCorrect, score: existing.score });
});

app.get("/leaderboard", (req, res) => {
  const sorted = leaderboard.sort((a, b) => b.score - a.score).slice(0, 5);
  res.json(sorted);
});

app.listen(PORT, () =>
  console.log(`Emoji game running at http://localhost:${PORT}`)
);
