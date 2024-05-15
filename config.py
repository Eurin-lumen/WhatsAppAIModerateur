# config.py
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')
SPAM_KEYWORDS = os.getenv('SPAM_KEYWORDS').split(',')
AD_PATTERNS = os.getenv('AD_PATTERNS').split(',')
