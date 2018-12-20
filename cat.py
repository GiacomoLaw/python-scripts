import json
import urllib.request
from selenium import webdriver

url = "https://api.thecatapi.com/v1/images/search"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

url = result[0]['url']

driver=webdriver.Chrome()
driver.get(url)