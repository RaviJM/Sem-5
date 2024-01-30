import requests
from bs4 import BeautifulSoup

# URL of the YouTube search results page
url = 'https://www.youtube.com/results?search_query=healthy+diet+recipes'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())

    # # Find and print all video links (they are usually in 'a' tags with 'href' attribute)
    # for link in soup.find_all('a', {'href': True}):
    #     href = link['href']
    #     print(href)
    #     if '/watch' in href:  # Check if it's a video link
    #         video_url = 'https://www.youtube.com' + href
    #         print(video_url)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
