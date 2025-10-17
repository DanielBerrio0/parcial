from models.users_model import User
from extensions import db

class UserRepository:
    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id: int):
        return User.query.filter_by(id=user_id).first()

    def create_user(self, username: str, password: str):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id: int, username: str = None, password: str = None):
        user = self.get_user_by_id(user_id)
        if user:
            if username:
                user.username = username
            if password:
                user.password = password
            db.session.commit()
            return user
        return None

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return None
