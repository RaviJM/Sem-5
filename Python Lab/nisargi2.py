import requests
from bs4 import BeautifulSoup
import time

url = "https://www.youtube.com/results?search_query=healthy+diet+recipes"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())

    # Find the elements containing video titles and links
    # video_elements = soup.find_all('a',{'class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'})
    # for article in video_elements:
    #     print(article)
    #
    #
    # # Extract video titles and links
    # recipe_recommendations = []
    # for video in video_elements:
    #     title = video['title']
    #     link = "https://www.youtube.com" + video['href']
    #     recipe_recommendations.append((title, link))
    #
    # print(f"Top 5 healthy recipe video recommendations:")
    # for i, (title, link) in enumerate(recipe_recommendations[:5], start=1):
    #     print(f"{i}. {title}")
    #     print(f"   Link: {link}\n")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


# Add a delay to avoid overloading the server
time.sleep(2)