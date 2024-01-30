import requests
from bs4 import BeautifulSoup

html_content = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"

soup = BeautifulSoup(html_content, "html.parser")

div = soup.div
for p in div.find_all('p'):
    print(p.text)