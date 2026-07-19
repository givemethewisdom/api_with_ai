"""jwt and hash logic"""
import hashlib

from app.core import config


class Security:
    """security class for hide sensitive data"""
    secret_key = config.secret_key

    def hash_data(self,data):
        """hash encrypted data"""
        #не хочу пользоваться hashlib. пока попробую сделать что-то простое сам
        return hashlib