import json
import os

USER_FILE = 'data/users.json'

# Simple file-based user authentication (You can replace this with a database like SQLite)
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

def authenticate_user(username, password):
    """Simple user authentication (replace with a more secure method if needed)."""
    users = load_users()
    if username in users and users[username] == password:
        return True
    return False

def register_user(username, password):
    """Register a new user."""
    users = load_users()
    if username not in users:
        users[username] = password
        save_users(users)
        return True
    return False
