from passlib.context import CryptContext

__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verfiy_password(plain_password: str, hashed_password: str):
    return __pwd_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password: str):
    return __pwd_context.hash(plain_password)
