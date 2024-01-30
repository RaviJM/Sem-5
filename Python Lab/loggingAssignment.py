# the project requires web scraping, so this assignment will be about logging related to web scraping

import requests
import logging

# configure logging
logging.basicConfig(filename="D:\\COLLEGE\\Python Lab\\Theory\\webScrapeLogFile.log", filemode="a", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# function to fetch the source code of the website (using proxy servers) and saving it to a html file
def fetchAndSaveToFile(url, path):
    try:
        r = requests.get(url)
        with open(path, "w", encoding="utf-8") as f:
            f.write(r.text)
            f.close()
            logging.info("Source code fetched successfully")

    except Exception as e:
        logging.error("Error occurred while fetching, opening or writing to file")

# IP and ports of available proxy servers [not used in project yet]
proxies = {
    "http": "109.254.21.27:9090",
    "https": "67.213.212.51:48986"
}

# url of website to be scraped
url = "https://timesofindia.indiatimes.com/india/chandrayaan-3-mission-pragyan-rover-discovers-sulphur-on-moon-why-its-significant/articleshow/103207669.cms"

# location of html file
path = "D:\\COLLEGE\\Python Lab\\Theory\\webIsScraped.html"

# function is called
fetchAndSaveToFile(url, path)
