// select all elements on the page
const elements = document.querySelectorAll("*");

// iterate over each element and invert its colors
elements.forEach(element => {
  // get the current color of the element
  const color = window.getComputedStyle(element).getPropertyValue("color");

  // invert the color using the invertColor function (defined below)
  const invertedColor = invertColor(color);

  // set the inverted color as the new color for the element
  element.style.color = invertedColor;

  // repeat the process for the background-color property
  const bgColor = window.getComputedStyle(element).getPropertyValue("background-color");
  const invertedBgColor = invertColor(bgColor);
  element.style.backgroundColor = invertedBgColor;
});

// define the invertColor function
function invertColor(color) {
  // if the color is transparent, return transparent
  if (color === "transparent") return color;

  // if the color is not a valid CSS color, return black
  if (!color.match(/^#(?:[0-9a-f]{3}){1,2}$/i)) return "#000000";

  // if the color is a valid CSS color, invert it using bitwise NOT
  return "#" + (0xFFFFFF ^ parseInt(color.slice(1), 16)).toString(16).padStart(6, "0");
}
