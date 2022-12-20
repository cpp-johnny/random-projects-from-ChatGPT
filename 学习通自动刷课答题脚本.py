pip install selenium


from selenium import webdriver

# create a new Chrome browser
driver = webdriver.Chrome()

# navigate to the learning platform
driver.get("https://www.xuexitong.com")


# find the username and password fields
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

# enter the username and password
username_field.send_keys("my_username")
password_field.send_keys("my_password")

# find the login button and click it
login_button = driver.find_element_by_name("login")
login_button.click()
