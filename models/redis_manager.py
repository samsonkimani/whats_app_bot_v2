import redis
import json

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def set_data(self, key, value, expire_time=None):
        try:
            data = json.dumps(value)
            self.redis_client.set(key, data)
            if expire_time:
                self.redis_client.expire(key, expire_time)
        except Exception as e:
            print(f"Error setting data in Redis: {str(e)}")

    def get_data(self, key):
        try:
            data = self.redis_client.get(key)
            if data:
                return data
        except Exception as e:
            print(f"Error getting data from Redis: {str(e)}")
        return None

    def delete_key(self, key):
        try:
            self.redis_client.delete(key)
        except Exception as e:
            print(f"Error deleting key in Redis: {str(e)}")

