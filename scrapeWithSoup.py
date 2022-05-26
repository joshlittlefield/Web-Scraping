from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?={in_currency}&to{out_currency}&amount=1'
    content = requests.get(url).text

    soup = BeautifulSoup(content, 'html.parser')
    conversion = soup.find('span', class_= 'ccOutputRslt').get_text()
    conversion = float(conversion[:-4])

    return conversion

print(get_currency('AUD','JPY'))