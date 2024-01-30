import requests
from bs4 import BeautifulSoup

homepage = 'https://news.google.com/'
url = 'https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor elements (<a>) and extract their href attributes
    links = []
    for anchor in soup.find_all('a', attrs={'aria-label': True, 'href': True}):
        label = anchor['aria-label']
        href = homepage+anchor['href']
        print(label+"   "+href)
        # href = anchor.get('href')
        # if href:
        #     links.append(href)

    # Print all the links
    for link in links:
        print()
        # print(link)
else:
    print(f'Failed to retrieve content. Status code: {response.status_code}')
