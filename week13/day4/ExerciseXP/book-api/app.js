const express = require("express");
const app = express();
const PORT = 5000;

app.use(express.json());

// Fake database
let books = [
  { 
    id: 1,
    title: "1984",
    author: "George Orwell",
    publishedYear: 1949
  },
  {
    id: 2,
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    publishedYear: 1960,
  },
];

// GET all books
app.get("/", (req, res) => {
  res.json(books);
});

// GET book by ID
app.get("/books/:bookId", (req, res) => {
  const book = books.find((b) => b.id === parseInt(req.params.bookId));
  if (!book) return res.status(404).json({ message: "Book not found" });
  res.status(200).json(book);
});

// POST create a new book
app.post("/books", (req, res) => {
  const newBook = {
    id: books.length + 1,
    title: req.body.title,
    author: req.body.author,
    publishedYear: req.body.publishedYear,
  };
  books.push(newBook);
  res.status(201).json(newBook);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
