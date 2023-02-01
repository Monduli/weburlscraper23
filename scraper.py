import requests
from bs4 import BeautifulSoup

def scraper(url):
    r = requests.get(url)
    print(r.content[:100])
    soup = BeautifulSoup(r.content, 'html.parser')