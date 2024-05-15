# bot.py
import config
from spam_detection.py import is_spam, is_advertisement
from warnings import warn_user

def handle_message(user_id, message):
    if is_spam(message) or is_advertisement(message):
        warn_user(user_id)

if __name__ == "__main__":
    # Simuler des messages entrants
    messages = [
        {"user_id": "user1", "message": "Check out this great sale! http://example.com"},
        {"user_id": "user2", "message": "Hello everyone!"},
        {"user_id": "user1", "message": "Promo code: DISCOUNT20"},
    ]

    for msg in messages:
        handle_message(msg['user_id'], msg['message'])
