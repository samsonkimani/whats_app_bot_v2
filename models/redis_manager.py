import redis
import json

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def set_data(self, key, value, expire_time=None):
        data = json.dumps(value)
        self.redis_client.set(key, data)
        if expire_time:
            self.redis_client.expire(key, expire_time)

    def get_data(self, key):
        data = self.redis_client.get(key)
        if data:
            return json.loads(data.decode('utf-8'))
        return None

    def delete_key(self, key):
        self.redis_client.delete(key)