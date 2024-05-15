# logging.py
import logging

logging.basicConfig(filename='moderation.log', level=logging.INFO)

def log_action(action, user_id, message=None):
    logging.info(f"Action: {action}, User ID: {user_id}, Message: {message}")
