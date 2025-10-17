from models.users_model import User
from sqlalchemy.orm import Session

class UserRepository:


    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_users(self):
   
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):

        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str):

        new_user = User(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, user_id: int, username: str = None, password: str = None):
 
        user = self.get_user_by_id(user_id)
        if user:
            if username:
                user.username = username
            if password:
                user.password = password
            self.db.commit()
            self.db.refresh(user)
            return user
        return None
    
    def delete_user(self, user_id: int):

        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return user
        return None
