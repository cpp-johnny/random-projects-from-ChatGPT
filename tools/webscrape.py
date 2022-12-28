# scraping data from https://advent-of-code.creator-spring.com/?

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
    
    # Find all the div tags with the class "item"
items = soup.find_all("div", class_="item")


# scrape link of each item
# Iterate over the items and extract the link
for item in items:
    # Find the link element within the item
    link_element = item.find("a")
    # Extract the link from the element
    link = link_element.get("href")
    print(link)
    
"""    
This will find all the div tags with the class "item", and then extract the link from the a tag within each div.

Keep in mind that the specific HTML tags and attributes you need to search for will depend on the structure of the website's HTML code. You may need to inspect the HTML code of the page to determine which tags and attributes contain the information you are interested in.

"""
