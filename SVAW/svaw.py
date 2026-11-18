#Importation des bibliotheques neccessaire au scanner.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

playloads = ["<script>alert(1)</script>",'<svg onload="alert(1)">','"><script>alert(1)</script>',"'><img src=X onerror=alert(1)>"]
url = input("[svaw] Veuillez entrer l'url du site a scanner : ")

#Introduction du scan

print("[svaw] Démarrage du scan : ", url)

def statut_url(url):
  reponse_site = requests.get(url, timeout = 5)
  statut_site = reponse_site.status_code
  return statut_site

#Validite du scan

if statut_url(url) != 200 :
   print("[svaw] Cible injoignable ou erreur HTTP (", statut_url(url))
else:  
   print("[svaw] Cible joignable (HTTP 200)")

def crawler(url) :
   reponse = requests.get(url, timeout = 5)
   Soupe = BeautifulSoup(reponse.text, "html.parser")
   return Soupe.find_all("input")

#Verification des zones d'entree

if crawler(url) :
   print("[svaw] Zone d'entree detecte")

   champs = crawler(url)
   listes = []
      
   for champ in champs :
       nom = champ.get("name")
       if nom is not None :
          listes.append(nom)
   print("[svaw] Liste des noms de zones d'entrees")
   print("[svaw]", listes)

   for liste in listes :
       reflet = 0
       for playload in playloads : 
           
           resultat = requests.get(url, params={liste : playload}, timeout = 5)
           print("[svaw] scan de la page", url, "en cours...")          
           if playload in resultat.text :
              reflet += 1 
              print("[svaw] Reflet possible au niveau de", liste)
                                 
else :
   print("[svaw] Aucune zone d'entree detecte")

#Remplissage des zones d'entrees dans la liste 

print("[svaw] Scan termine :", reflet, "reflet(s) trouve(s)")
