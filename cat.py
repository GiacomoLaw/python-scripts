import json
import urllib.request
import webbrowser

url = "https://api.thecatapi.com/v1/images/search"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

url = result[0]['url']

webbrowser.open(url)