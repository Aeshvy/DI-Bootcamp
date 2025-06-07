function myMove() {
  const elem = document.getElementById("animate");
  let pos = 0;
  const maxPos = 400 - 50;

  const id = setInterval(frame, 1);

  function frame() {
    if (pos >= maxPos) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.left = pos + "px";
    }
  }
}
