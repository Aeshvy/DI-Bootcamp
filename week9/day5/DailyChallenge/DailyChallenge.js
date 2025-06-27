// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
watch() {
    console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}
// Instantiate a new Video instance and call the watch() method.
const firstVideo = new Video("Learning JavaScript", "Alice", 300);

// Instantiate a second Video instance with different values.
const secondVideo = new Video("Understanding OOP", "Bob", 600);