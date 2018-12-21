import urllib.request
from bs4 import BeautifulSoup

url = input("What URL do you want to scrape? ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# remove all script and style elements
for script in soup(["script", "style"]):
	script.extract()

# get text
text = soup.get_text()

print(text)
