import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
URL = "https://www.cigogne-management.com/fr/bank/cm/-/sie-98-xs3184046822"
reponse = requests.get(URL)

idx = reponse.text.find("100578")
print(reponse.text[idx-300:idx+200])

matche = re.search(r"data:(\[\[.*?\]\])",reponse.text)
data = json.loads(matche.group(1))

dateenms,valeur = data[-1]

date_final = datetime.fromtimestamp(dateenms/1000)
print(data)
print(valeur)
print(date_final)

dico={}


    

with open("Scraper_stork.csv","w",encoding = "utf-8") as l:
    for key,val in data:
    
        key_dico = datetime.fromtimestamp(key/1000)+timedelta(hours=2)
        dico[key_dico] = val
        ligne = f"{key_dico};{str(val)}\n"
        l.write(ligne)