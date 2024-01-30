from bs4 import BeautifulSoup
# Sample HTML content
html_content = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
# Find all list items
items = soup.find_all("li")
# Print each item
for item in items:
    print(item.text)
