# warnings.py
from ban_user import ban_user


user_warnings = {}

def warn_user(user_id):
    if user_id not in user_warnings:
        user_warnings[user_id] = 0
    user_warnings[user_id] += 1
    
    if user_warnings[user_id] == 1:
        print(f"User {user_id} has been warned for the first time.")
    elif user_warnings[user_id] == 2:
        print(f"User {user_id} has been warned for the second time.")
    else:
        ban_user(user_id)
