function authenticate() {
  // get the username and password from the form
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;

  // check if the username and password are valid
  if (username === 'admin' && password === 'password') {
    // if valid, redirect to the dashboard page
    window.location.href = 'dashboard.html';
  } else {
    // if not valid, display an error message
    alert('Invalid username or password');
  }
}
