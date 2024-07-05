from flask import Flask, jsonify, request
from user_service import UserService
from redis_client import RedisClient
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

app = Flask(__name__)

redis_client = RedisClient()
user_service = UserService(redis_client)


@app.route('/api/user', methods=['POST', 'GET'])
def manage_user():
    if request.method == 'POST':
        user_details = request.json
        if not user_details:
            return jsonify({'error': 'User details are required'}), 400

        user_data, error = user_service.create_user(user_details)
        if error:
            return jsonify({'message': error}), 200
        return jsonify({'message': 'User added', 'details': user_data}), 200

    elif request.method == 'GET':
        user_id, user_details = user_service.retrieve_user()
        if user_id:
            return jsonify({'user_id': user_id, 'details': user_details}), 200
        else:
            return jsonify({'message': 'No unused users available.'}), 200


@app.route('/api/user/list', methods=['GET'])
def list_users():
    user_details_list = user_service.list_users()
    return jsonify({'users': user_details_list}), 200


@app.route('/api/user-pool', methods=['GET'])
def user_pool():
    fill = request.args.get('fill')
    flush = request.args.get('flush')

    if fill:
        try:
            count = int(fill)
            user_service.fill_user_pool(count)
            return jsonify({'message': f'{count} users added to the pool.'}), 200
        except ValueError:
            return jsonify({'error': 'Invalid fill count'}), 400

    if flush is not None:
        user_service.flush_user_pool()
        return jsonify({'message': 'All users flushed from the pool.'}), 200

    return jsonify({'error': 'No valid query parameter provided'}), 400


if __name__ == '__main__':
    flask_config = config['flask']
    app.run(debug=True, host=flask_config['host'], port=flask_config['port'])