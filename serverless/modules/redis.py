import logging
from redis import Redis


class Redis:
    def __init__(self):
        self.nodes = []

    def get_pool(self):
        self.redis = Redis(host='localhost', port=6379, db=0)
    
    def get_keys(self, key_name="*") -> list:
        return self.redis.scan_iter(
            match=f"{key_name}",
            count=100
        )
    
    def get_ping(self) -> bool:
        return self.redis.ping()
    
    def get(self, key: str) -> str:
        value = self.redis.get(key)
        logging.info(f"Redis get: {key} = {value}")
        return value
    
    def _set(self, key: str, value: str) -> dict:
        try:
            self.redis.set(key, value)
        except Exception as e:
            logging.error(f"Redis set: {key} = {value}")
            logging.error(e)
            raise e
        logging.info(f"Redis set: {key} = {value}")
        return {"key": key, "value": value}
    
    def setex(self, key: str, value: str, ttl: int) -> dict:
        try:
            self.redis.setex(key, value, ttl)
        except Exception as e:
            logging.error(f"Redis setex: {key} = {value}")
            logging.error(e)
            raise e
        logging.info(f"Redis setex [ttl {ttl}]: {key} = {value}")
        return {"key": key, "value": value}

def get_redis() -> Redis:
    r = Redis()
    r.get_pool()
    return r