# bot.py
import config
from spam_detection import is_spam, is_advertisement
from warnings import warn_user
from moderation_requests import report_message, handle_report
from logging import log_action
from assistance_requests import request_assistance
from statistics import generate_report
from admin_notifications import notify_admin
from ml_model import SpamClassifier

def handle_message(user_id, message):
    if is_spam(message) or is_advertisement(message):
        warn_user(user_id)
        log_action('warn', user_id, message)

if __name__ == "__main__":
    # Simuler des messages entrants
    messages = [
        {"user_id": "user1", "message": "Check out this great sale! http://example.com"},
        {"user_id": "user2", "message": "Hello everyone!"},
        {"user_id": "user1", "message": "Promo code: DISCOUNT20"},
    ]

    for msg in messages:
        handle_message(msg['user_id'], msg['message'])
