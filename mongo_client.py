from pymongo import MongoClient as PyMongoClient
import yaml


class MongoClient:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        mongo_config = config['mongodb']
        self.client = PyMongoClient(
            host=mongo_config['host'],
            port=mongo_config['port']
        )
        self.db = self.client[mongo_config['db']]
        self.users_collection = self.db['users']

    def add_user(self, user_id, user_details):
        if not self.users_collection.find_one({"user_id": user_id}):
            user_details['user_id'] = user_id
            self.users_collection.insert_one(user_details)
            return True
        return False

    def get_user(self):
        user = self.users_collection.find_one_and_delete({})
        if user:
            user_id = user['user_id']
            del user['_id']
            return user_id, user
        return None, None

    def list_users(self):
        users = self.users_collection.find()
        user_details_list = []
        for user in users:
            del user['_id']
            user_details_list.append(user)
        return user_details_list

    def flush_users(self):
        self.users_collection.delete_many({})