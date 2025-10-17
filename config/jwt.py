
from datetime import timedelta

JWT_SECRET_KEY = "superclave-ultra-secreta-12345"
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"
