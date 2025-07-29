import requests
from bs4 import BeautifulSoup

# İstanbul'daki satılık daire ilanları (örnek URL)
url = "https://www.sahibinden.com/satilik-daire/istanbul"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# İlan başlıklarını çek
titles = soup.select("td.searchResultsTitleValue a")

print("İstanbul'daki Satılık Daire İlan Başlıkları:\n")
for title in titles[:10]:  # İlk 10 ilan
    print("-", title.text.strip())