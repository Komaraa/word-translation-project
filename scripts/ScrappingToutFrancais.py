from typing import Counter
import requests
from bs4 import BeautifulSoup
import html
import unicodedata

list_elements_filtrer = []

urls = "https://simple.wikipedia.org/wiki/Wikipedia:BASIC_English_alphabetical_wordlist"

response2 = requests.get(urls)
response2.encoding = 'utf-8'
soup2 = BeautifulSoup(response2.text, 'html.parser')
links2 = soup2.find_all('a',class_='extiw')

for link in links2:
    # Décoder les entités HTML
    decode_text = html.unescape(link.get_text())
    # Normaliser les caractères spéciaux
    normalized_text = unicodedata.normalize("NFKC", decode_text)
    list_elements_filtrer.append(normalized_text)


compteur = Counter(list_elements_filtrer)

# Extraire les doublons
simple = [item for item, count in compteur.items() if count == 1]
print(simple)

# Ecrire dans un fichier txt les mots anglais
with open('english_words.txt_4', 'w', encoding='utf-8') as file:
    for item in simple:
        file.write("%s\n" % item)