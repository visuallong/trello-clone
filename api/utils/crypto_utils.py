from passlib.context import CryptContext

class CryptoUtil:
    def __init__(self) -> None:
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verfiy_password(self,plain_password: str, hashed_password: str):
        return self.__pwd_context.verify(plain_password, hashed_password)


    def get_password_hash(self,plain_password: str):
        return self.__pwd_context.hash(plain_password)