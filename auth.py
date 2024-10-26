import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException
from config import SECRET_KEY, ALGORITHM

class Autenticacion:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        print("se inicio la clase correctamente")

    def create_jwt_token(self, data: dict):
        expiration = datetime.utcnow() + timedelta(hours=1)  # Token válido por 1 hora
        to_encode = data.copy()
        to_encode.update({"exp": expiration})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_jwt_token(self, token: str):
        try:
            decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print("el token ha sido validado exitosamente::::::::::::::::")
            return decoded_jwt
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="El token ha expirado",
                headers={"WWW-Authenticate": "Bearer"}
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"}
            )

    def verify_password(self, plain_password, mi_hashed_password):
        hashed_password = self.pwd_context.hash(mi_hashed_password)
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def authenticate_user(self, base, username: str, password: str):
        user = base.get(username)
        if not user:
            return False
        if not self.verify_password(password, user['password']):
            return False
        return user
