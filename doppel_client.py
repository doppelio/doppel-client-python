import requests
import json

class DoppelClient:
    def __init__(self, application_id, api_key):
        self.application_id = application_id
        self.api_key = api_key

        self.host = 'http:localhost:8080'

        self.headers = ''
        self.update_headers()

    def perform_request(self, method, path, params=None, data=None):
        url = self.host + path
        if params:
            self.add_params(url, params)
        return requests.request(method, url, headers=self.headers, json=data).json()

    def add_params(self, url, params):
        return url + '?' + '&'.join(key + '=' + str(value) for key, value in params.items())

    def update_headers(self):
        return {
            'X-Doppel-API-Key': self.api_key,
            'X-Doppel-Application-ID': self.application_id,
            'Content-Type': 'application/json',
        }

	def get_users(self, params=None):
		path = '/' + 'users/'
		return self.perform_request('GET', path, params=params)

	def add_user(self, user):
		path = '/' + 'users/'
		return self.perform_request('POST', path, data=user)

	def get_user(self, user_id):
		path = '/' + 'users/' + user_id + '/'
		return self.perform_request('GET', path)

	def save_user(self, user):
		path = '/' + 'users/' + user['userID'] + '/'
		return self.perform_request('PUT', path, data=user)

	def update_user(self, partial_user):
		path = '/' + 'users/' + partial_user['userID'] + '/'
		return self.perform_request('PATCH', path, data=partial_user)

	def delete_user(self, user_id):
		path = '/' + 'users/' + user_id + '/'
		return self.perform_request('DELETE', path)

	def get_user_ratings(self, user_id):
		path = '/' + 'users/' + user_id + '/' + 'ratings/'
		return self.perform_request('GET', path)

	def get_rating(self, user_id, item_id):
		path = '/' + 'users/' + user_id + '/' + 'ratings/' + item_id + '/'
		return self.perform_request('GET', path)

	def save_rating(self, rating):
		path = '/' + 'users/' + rating['userID'] + '/' + 'ratings/' + rating['itemID'] + '/'
		return self.perform_request('PUT', path, data=rating)

	def delete_rating(self, user_id, item_id):
		path = '/' + 'users/' + user_id + '/' + 'ratings/' + item_id + '/'
		return self.perform_request('DELETE', path)

	def get_prediction(self, user_id, item_id):
		path = '/' + 'users/' + user_id + '/' + 'predictions/' + item_id + '/'
		return self.perform_request('GET', path)

	def get_user_recommendations(self, user_id):
		path = '/' + 'users/' + user_id + '/' + 'recommendations/'
		return self.perform_request('GET', path)

	def get_similar_users(self, user_id):
		path = '/' + 'users/' + user_id + '/' + 'similars/'
		return self.perform_request('GET', path)

	def get_users_similarity(self, user_id, other_user_id):
		path = '/' + 'users/' + user_id + '/' + 'similarities/' + other_user_id + '/'
		return self.perform_request('GET', path)

	def get_items(self, params=None):
		path = '/' + 'items/'
		return self.perform_request('GET', path, params=params)

	def add_item(self, item):
		path = '/' + 'items/'
		return self.perform_request('POST', path, data=item)

	def get_item(self, item_id):
		path = '/' + 'items/' + item_id + '/'
		return self.perform_request('GET', path)

	def save_item(self, item):
		path = '/' + 'items/' + item['itemID'] + '/'
		return self.perform_request('PUT', path, data=item)

	def update_item(self, partial_item):
		path = '/' + 'items/' + partial_item['itemID'] + '/'
		return self.perform_request('PATCH', path, data=partial_item)

	def delete_item(self, item_id):
		path = '/' + 'items/' + item_id + '/'
		return self.perform_request('DELETE', path)

	def get_item_ratings(self, item_id):
		path = '/' + 'items/' + item_id + '/' + 'ratings/'
		return self.perform_request('GET', path)

	def get_item_recommendations(self, item_id):
		path = '/' + 'items/' + item_id + '/' + 'recommendations/'
		return self.perform_request('GET', path)

	def get_similar_items(self, item_id):
		path = '/' + 'items/' + item_id + '/' + 'similars/'
		return self.perform_request('GET', path)

	def get_items_similarity(self, item_id, other_item_id):
		path = '/' + 'items/' + item_id + '/' + 'similarities/' + other_item_id + '/'
		return self.perform_request('GET', path)

