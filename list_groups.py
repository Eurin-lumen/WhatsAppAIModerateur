# list_groups.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Chemin vers le driver (modifiez ce chemin selon l'emplacement de votre driver)
driver_path = 'path/to/chromedriver'

# Initialiser le driver
driver = webdriver.Chrome(executable_path=driver_path)

# Ouvrir WhatsApp Web
driver.get('https://web.whatsapp.com')

# Attendre que l'utilisateur scanne le QR code
input("Appuyez sur Entrée après avoir scanné le QR code")

# Attendre le chargement de l'interface
time.sleep(10)

# Rechercher tous les groupes
group_elements = driver.find_elements(By.XPATH, '//span[@class="_3m_Xw"]')

print("List of groups:")
for group in group_elements:
    group_name = group.text
    group.click()
    time.sleep(2)
    group_id = driver.current_url.split('/')[-1]
    print(f"Name: {group_name}, ID: {group_id}")

# Fermer le driver
driver.quit()
