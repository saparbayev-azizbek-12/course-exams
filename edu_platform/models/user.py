import hashlib
from datetime import datetime

class Role:
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password: str, stored_hash: str) -> bool:
    return hash_password(input_password) == stored_hash

class User:
    users = []
    def __init__(self, id, full_name, email, password, role):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = hash_password(password)
        self.role = role
        self._notifications = []
        self.created_at = datetime.now()
        User.users.append(self)

    def add_notification(self, message):
        self._notifications.append(message)

    def view_notifications(self):
        return self._notifications

    def delete_notification(self, id):
        if 0 <= id < len(self._notifications):
            del self._notifications[id]
            return True
        return False

    def objects(self):
        return User.users
