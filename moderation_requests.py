# moderation_requests.py
def report_message(user_id, message_id):
    # Logique pour signaler un message
    print(f"Message {message_id} reported by user {user_id}.")

def handle_report(admin_id, message_id, action):
    # Logique pour gérer les signalements
    if action == 'delete':
        print(f"Message {message_id} deleted by admin {admin_id}.")
    elif action == 'ban':
        print(f"User associated with message {message_id} banned by admin {admin_id}.")
