function makeSandwich() {
  var bread = document.getElementById("bread").value;
  var meat = document.getElementById("meat").value;
  var cheese = document.getElementById("cheese").value;
  var lettuce = document.getElementById("lettuce").checked;
  var tomato = document.getElementById("tomato").checked;
  var mayo = document.getElementById("mayo").checked;
  var sandwich = "Your sandwich has " + bread + " bread, " + meat + " meat, and " + cheese + " cheese. ";
  if (lettuce) {
    sandwich += "It also has lettuce. ";
  }
  if (tomato) {
    sandwich += "It also has tomato. ";
  }
  if (mayo) {
    sandwich += "It also has mayo. ";
  }
  document.getElementById("sandwich").innerHTML = sandwich;
}
