import requests
from bs4 import BeautifulSoup

# The URL of the page you want to scrape
url = "https://www.eatingwell.com/recipes/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the anchor tags with links to recipes
recipe_links = soup.find_all('a', class_='view-all')
print(recipe_links)
# Extract and print the recipe links
for link in recipe_links:
    recipe_link = link.get('href')
    print(f'https://www.eatingwell.com{recipe_link}')