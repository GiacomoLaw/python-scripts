import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://api.monzo.com/crowdfunding-investment/total"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

if 'invested_amount' in text:
    result = text.split(",")

invested = str(result[1])
investedn = invested.split(':')[1]
plainnum = int(str(investedn)[:-4])
number = "{:,}".format(int(plainnum))

print("£",number)