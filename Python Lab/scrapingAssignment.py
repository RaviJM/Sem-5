from bs4 import BeautifulSoup

filePath = "D:\\COLLEGE\\Web Technology Lab\\prac2.html"
fp = open(filePath, 'r', encoding="utf-8")
html = fp.read()
soup = BeautifulSoup(html, 'html.parser')

# printing all the content of html file
print("Printing all the content of html file")
print(soup)
print("\n\n")

# printing title
print("Title: ", soup.title.text)
print("\n\n")

# printing title
print("Heading: ", soup.h1.text)
print("\n\n")

# printing all the paragraphs
print("All paragraphs in html file")
paragraphsList = soup.find_all('p')
for paragraph in paragraphsList:
    print(paragraph.text)
print("\n\n")

# printing address
print("Addresses in the html file: ", soup.address.text)
print("\n\n")

# printing quotation text
print("Quatation texts: ", )
quotes = soup.find_all('q')
for quote in quotes:
    print(quote.text)
print("\n\n")

# printing italic text
print("Italic texts in html file: ", )
italics = soup.find_all('i')
for italic in italics:
    print(italic.text)
print("\n\n")

# printing bold text
print("Bold texts in html file: ", )
bolds = soup.find_all('b')
for bold in bolds:
    print(bold.text)
print("\n\n")