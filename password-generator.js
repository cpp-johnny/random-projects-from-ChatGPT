function generatePassword() {
  // Set the password length
  const passwordLength = 10;

  // Set the possible password characters
  const passwordChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";

  // Initialize the password variable
  let password = "";

  // Generate a random password
  for (let i = 0; i < passwordLength; i++) {
    // Get a random character from the passwordChars string
    const randomChar = passwordChars.charAt(Math.floor(Math.random() * passwordChars.length));

    // Append the random character to the password
    password += randomChar;
  }

  // Return the password
  return password;
}

// Generate a password and print it to the console
const password = generatePassword();
console.log(password);
