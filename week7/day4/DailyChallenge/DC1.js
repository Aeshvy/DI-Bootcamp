// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.
var sentence = "The movie is not that bad, I like it";
console.log(sentence);

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).
var wordNot = sentence.indexOf("not");
console.log(wordNot);

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).
var wordBad = sentence.indexOf("bad");
console.log(wordBad);

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
if (wordBad > wordNot && wordNot !== -1 && wordBad !== -1) {
  var result =
    sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  console.log(result);
} else {
  console.log(sentence);
}
