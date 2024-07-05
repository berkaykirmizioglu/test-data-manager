import redis
import yaml


class RedisClient:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        redis_config = config['redis']
        self.client = redis.Redis(
            host=redis_config['host'],
            port=redis_config['port'],
            db=redis_config['db'],
            decode_responses=True
        )

    def add_user(self, user_id, user_details):
        if not self.client.sismember('users', user_id):
            self.client.sadd('users', user_id)
            self.client.hmset(f'user:{user_id}', user_details)
            return True
        return False

    def get_user(self):
        user_id = self.client.spop('users')
        if user_id:
            user_details = self.client.hgetall(f'user:{user_id}')
            self.client.delete(f'user:{user_id}')
            return user_id, user_details
        return None, None

    def list_users(self):
        users = self.client.smembers('users')
        user_details_list = []
        for user_id in users:
            user_details = self.client.hgetall(f'user:{user_id}')
            user_details_list.append({'user_id': user_id, 'details': user_details})
        return user_details_list

    def flush_users(self):
        keys = self.client.smembers('users')
        for key in keys:
            self.client.delete(f'user:{key}')
        self.client.delete('users')