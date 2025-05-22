const colors = [
  "#FF0000",
  "#FF7F00",
  "#FFFF00",
  "#00FF00",
  "#0000FF",
  "#4B0082",
  "#8B00FF",
  "#FFFFFF",
  "#C0C0C0",
  "#808080",
  "#000000",
  "#A52A2A",
  "#FFA500",
  "#FFC0CB",
  "#ADD8E6",
];
let selectedColor = colors[0];
let isMouseDown = false;

document.addEventListener("DOMContentLoaded", () => {
  const colorPaletteContainer = document.querySelector(
    "#color-palette .color-grid"
  );
  const gridContainer = document.getElementById("grid-container");
  const clearButton = document.getElementById("clear-button");

  function createColorPalette() {
    if (!colorPaletteContainer) return;
    colorPaletteContainer.innerHTML = "";
    colors.forEach((color) => {
      const swatch = document.createElement("div");
      swatch.classList.add("color-swatch");
      swatch.style.backgroundColor = color;
      swatch.dataset.color = color;

      if (color === selectedColor) {
        swatch.classList.add("selected");
      }

      swatch.addEventListener("click", () => {
        selectedColor = swatch.dataset.color;
        document
          .querySelectorAll(".color-swatch")
          .forEach((s) => s.classList.remove("selected"));
        swatch.classList.add("selected");
      });

      colorPaletteContainer.appendChild(swatch);
    });
  }

  /**
@param {number} size
     */

  function createGrid(size) {
    if (!gridContainer) return;
    gridContainer.innerHTML = "";

    gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
    gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;

    const totalCells = size * size;
    for (let i = 0; i < totalCells; i++) {
      const cell = document.createElement("div");
      cell.classList.add("grid-cell");

      cell.addEventListener(
        "touchstart",
        (e) => {
          isMouseDown = true;
          e.preventDefault();
          paintCell(e.target);
        },
        { passive: false }
      );

      cell.addEventListener(
        "touchmove",
        (e) => {
          if (isMouseDown) {
            e.preventDefault();
            const touch = e.touches[0];
            const element = document.elementFromPoint(
              touch.clientX,
              touch.clientY
            );
            paintCell(element);
          }
        },
        { passive: false }
      );

      cell.addEventListener("mousedown", (e) => {
        isMouseDown = true;
        paintCell(e.target);
      });

      cell.addEventListener("mouseover", (e) => {
        if (isMouseDown) {
          paintCell(e.target);
        }
      });

      cell.addEventListener("dragstart", (e) => e.preventDefault());

      gridContainer.appendChild(cell);
    }
  }

  /**
   * @param {HTMLElement} cell
   */

  function paintCell(cell) {
    if (cell && cell.classList.contains("grid-cell")) {
      cell.style.backgroundColor = selectedColor;
    }
  }

  function clearGrid() {
    if (!gridContainer) return;
    const cells = gridContainer.querySelectorAll(".grid-cell");
    cells.forEach((cell) => {
      cell.style.backgroundColor = "#ffffff";
    });
  }

  document.addEventListener("mouseup", () => {
    if (isMouseDown) {
      isMouseDown = false;
    }
  });
  document.addEventListener("touchend", () => {
    if (isMouseDown) {
      isMouseDown = false;
    }
  });

  document.body.addEventListener("selectstart", (e) => {
    if (isMouseDown) {
      e.preventDefault();
    }
  });

  if (clearButton) {
    clearButton.addEventListener("click", clearGrid);
  }
  createColorPalette();
  createGrid(30);
});
