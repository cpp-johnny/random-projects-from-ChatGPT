// Use the Date object to get the current time
let now = new Date();

// Get the hours from the Date object
let hours = now.getHours();

// Print a greeting based on the time of day
if (hours >= 6 && hours < 12) {
  console.log("Good morning!");
} else if (hours >= 12 && hours < 18) {
  console.log("Good afternoon!");
} else {
  console.log("Good evening!");
}
