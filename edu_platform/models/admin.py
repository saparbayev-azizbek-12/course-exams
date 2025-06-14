import pandas as pd
from .user import User, Role

class Admin(User):
    def __init__(self, id, full_name, email, password, role: Role):
        super().__init__(id, full_name, email, password, role)
        self.admin_id = id
        self.permissions = []

    def add_user(self, full_name, email, password, _role):
        role = None
        _role = int(_role)
        id = len(User.users) + 1
        if _role == 1:
            role = Role.ADMIN
        elif _role == 2:
            role = Role.TEACHER
        elif _role == 3:
            role = Role.STUDENT
        elif _role == 4:
            role = Role.PARENT
        User(id, full_name, email, password, role)
        pd.DataFrame([user.__dict__ for user in User.users]).to_csv("data/users.csv", index=False)
        self.add_notification(f"Yangi foydalanuvchi qo'shildi: {full_name}")
        return f"Foydalanuvchi {full_name} qo'shildi!"

    def remove_user(self, id):
        users = pd.read_csv('data/users.csv')
        for index, user in users.iterrows():
            if user.id == id:
                users = users.drop(index)
                users.to_csv('data/users.csv', index=False)
                return True
        return False

    def generate_report(self):
        users = pd.read_csv('data/users.csv')
        return users[['id', 'full_name']].to_string(index=False)