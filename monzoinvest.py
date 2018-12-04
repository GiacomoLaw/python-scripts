# update based on https://gist.github.com/lumisota/86663e0020825332075b67dd8d889f1f
import requests

url = "https://api.monzo.com/crowdfunding-investment/total"
data = requests.get(url).json()

plainnum = int(str(data["invested_amount"])[:-4])
number = "{:,}".format(int(plainnum))

print("£",number)