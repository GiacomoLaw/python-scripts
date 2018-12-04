# based on https://github.com/GiacomoLaw/Python-scripts/blob/master/monzoinvest.py
import requests

url = "https://api.monzo.com/crowdfunding-investment/total"
data = requests.get(url).json()

plainnum = int(str(data["invested_amount"])[:-4])
number = "{:,}".format(int(plainnum))

print("£",number)