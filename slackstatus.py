import urllib.request
from bs4 import BeautifulSoup

url = 'https://status.slack.com/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# remove all script and style elements
for script in soup(["script", "style"]):
	script.extract()

text = soup.get_text()

if "Slack is up and running" in text:
	print("Online")

else:
	print("Something is wrong")
