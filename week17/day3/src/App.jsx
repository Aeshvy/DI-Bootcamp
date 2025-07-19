import React, { useState } from 'react';
import quotes from './quotes';
import './App.css';

const getRandomIndex = (excludeIndex) => {
  let index;
  do {
    index = Math.floor(Math.random() * quotes.length);
  } while (index === excludeIndex);
  return index;
};

const getRandomColor = () =>
  `hsl(${Math.floor(Math.random() * 360)}, 60%, 60%)`;

function App() {
  const [currentIndex, setCurrentIndex] = useState(
    Math.floor(Math.random() * quotes.length)
  );
  const [colors, setColors] = useState({
    background: getRandomColor(),
    quoteText: getRandomColor(),
    buttonColor: getRandomColor(),
  });

  const handleNewQuote = () => {
    const newIndex = getRandomIndex(currentIndex);
    setCurrentIndex(newIndex);
    setColors({
      background: getRandomColor(),
      quoteText: getRandomColor(),
      buttonColor: getRandomColor(),
    });
  };

  const currentQuote = quotes[currentIndex];

  return (
    <div
      className="app"
      style={{ backgroundColor: colors.background }}
    >
      <div className="quote-box">
        <h1 style={{ color: colors.quoteText }}>
          "{currentQuote.quote}"
        </h1>
        <p className="author">– {currentQuote.author || 'Unknown'}</p>
        <button
          style={{ backgroundColor: colors.buttonColor }}
          onClick={handleNewQuote}
        >
          New quote
        </button>
      </div>
    </div>
  );
}

export default App;
