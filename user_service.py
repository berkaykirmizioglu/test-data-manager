from faker import Faker


class UserService:
    def __init__(self, redis_client):
        self.redis_client = redis_client
        self.fake = Faker()

    def create_user(self, user_details):
        user_id = user_details.get('user_id')
        if not user_id:
            return None, 'User ID is required'

        user_details.update({
            'username': self.fake.user_name(),
            'email': self.fake.email(),
            'name': self.fake.first_name(),
            'surname': self.fake.last_name(),
            'gender': self.fake.random_element(elements=('male', 'female'))
        })

        if self.redis_client.add_user(user_id, user_details):
            return user_details, None
        else:
            return None, 'User already exists'

    def retrieve_user(self):
        return self.redis_client.get_user()

    def list_users(self):
        return self.redis_client.list_users()

    def fill_user_pool(self, count):
        for _ in range(count):
            user_id = self.fake.uuid4()
            user_details = {
                'username': self.fake.user_name(),
                'email': self.fake.email(),
                'name': self.fake.first_name(),
                'surname': self.fake.last_name(),
                'gender': self.fake.random_element(elements=('male', 'female'))
            }
            self.redis_client.add_user(user_id, user_details)

    def flush_user_pool(self):
        self.redis_client.flush_users()
