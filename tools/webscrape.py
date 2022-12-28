// scraping data from https://advent-of-code.creator-spring.com/?

import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website and retrieve the HTML content
url = "https://advent-of-code.creator-spring.com/"
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract the data you are interested in
# For example, you can extract all the links on the page using the "a" tag
links = soup.find_all("a")
for link in links:
    print(link.get("href"))
