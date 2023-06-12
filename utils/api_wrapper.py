import requests
from pydantic import ValidationError


class APIWrapper:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.token = None
        self.timeout = timeout

    def set_token(self, token):
        self.token = token

    def _get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _get(self, endpoint):
        url = self.base_url + endpoint
        headers = self._get_headers()
        response = requests.get(url, headers=headers, timeout=self.timeout)
        return response

    def _post(self, endpoint, data):
        url = self.base_url + endpoint
        headers = self._get_headers()
        response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
        return response

    def _put(self, endpoint, data):
        url = self.base_url + endpoint
        headers = self._get_headers()
        response = requests.put(url, json=data, headers=headers, timeout=self.timeout)
        return response

    def _delete(self, endpoint):
        url = self.base_url + endpoint
        headers = self._get_headers()
        response = requests.delete(url, headers=headers, timeout=self.timeout)
        return response

    def get(self, endpoint):
        response = self._get(endpoint)
        return response

    def post(self, endpoint, data):
        response = self._post(endpoint, data)
        return response

    def put(self, endpoint, data):
        response = self._put(endpoint, data)
        return response

    def delete(self, endpoint):
        response = self._delete(endpoint)
        return response

    @staticmethod
    def parse_response(response, model):
        try:
            if response.status_code == 200:
                return model.parse_obj(response.json())
            elif response.status_code == 204:
                return None
        except ValidationError:
            return None

    def get_resource(self, endpoint, model):
        response = self.get(endpoint)
        return self.parse_response(response, model)

    def get_resource_list(self, endpoint, model):
        response = self.get(endpoint)
        try:
            if response.status_code == 200:
                return [model.parse_obj(item) for item in response.json()]
        except ValidationError:
            return []

    def create_resource(self, endpoint, data, model):
        response = self.post(endpoint, data)
        return self.parse_response(response, model)

    def update_resource(self, endpoint, data, model):
        response = self.put(endpoint, data)
        return self.parse_response(response, model)

    def delete_resource(self, endpoint):
        response = self.delete(endpoint)
        return response.status_code
