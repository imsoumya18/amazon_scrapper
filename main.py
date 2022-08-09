import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.77 Safari/537.36"}
res = requests.get('https://icy.tools', headers=headers, timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

rows = soup.find('tbody').find_all('tr')[:5]

for i in rows:
    name = i.find('td').find('a').find('div').find_all('div')[1].find('p').text
    sales = i.find_all('td')[2].find('a').find('div').find(text=True, recursive=False)
