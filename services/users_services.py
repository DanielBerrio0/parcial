import logging
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.users_model import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UsersService:
    def __init__(self):
        pass

    def authenticate_user(self, username: str, password: str):
        """
        Buscar usuario por username y verificar la contraseña (hash).
        Retorna el objeto User si coincide, o None si no.
        """
        logger.info(f"Authenticating user: {username}")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            logger.info(f"User authenticated successfully: {username}")
            return user
        logger.warning(f"Failed authentication attempt for username: {username}")
        return None

    def get_all_users(self):
        """Retorna lista de todos los usuarios."""
        logger.info("Fetching all users")
        return User.query.all()

    def get_user_by_id(self, user_id: int):
        """Retorna un usuario por su id o None si no existe."""
        logger.info(f"Fetching user by id: {user_id}")
        return User.query.get(user_id)

    def create_user(self, username: str, password: str):
        """
        Crea un usuario con contraseña hasheada.
        Retorna el objeto User creado.
        """
        logger.info(f"Creating user: {username}")
        password_hashed = generate_password_hash(password)
        new_user = User(username=username, password=password_hashed)
        db.session.add(new_user)
        db.session.commit()
        # refresh no es estrictamente necesario con flask_sqlalchemy, pero lo dejamos seguro:
        db.session.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, username: str = None, password: str = None):
        """
        Actualiza username y/o password (si se entregan).
        Retorna el usuario actualizado o None si no existe.
        """
        logger.info(f"Updating user id: {user_id}")
        user = self.get_user_by_id(user_id)
        if not user:
            logger.warning(f"User id {user_id} not found for update")
            return None

        if username:
            user.username = username
        if password:
            user.password = generate_password_hash(password)

        db.session.commit()
        db.session.refresh(user)
        return user

    def delete_user(self, user_id: int):
        """
        Elimina un usuario. Retorna el usuario eliminado o None si no existe.
        """
        logger.info(f"Deleting user id: {user_id}")
        user = self.get_user_by_id(user_id)
        if not user:
            logger.warning(f"User id {user_id} not found for delete")
            return None

        db.session.delete(user)
        db.session.commit()
        return user
