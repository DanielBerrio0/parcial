# config/jwt.py
from datetime import timedelta

JWT_SECRET_KEY = "superclave-ultra-secreta-12345"  # <-- cámbiala a algo largo y seguro
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"
