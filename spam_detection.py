# spam_detection.py
import re

def is_spam(message):
    spam_keywords = ['spam', 'advertisement', 'promo']
    return any(keyword in message.lower() for keyword in spam_keywords)

def is_advertisement(message):
    ad_patterns = [r'http[s]?://', r'\bdiscount\b', r'\bsale\b']
    return any(re.search(pattern, message.lower()) for pattern in ad_patterns)
