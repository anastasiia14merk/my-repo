import requests

from endpoints.base_endpoint import BaseEndpoint

class PostAuthorise(BaseEndpoint):
    def authorise(self, name):
        body = {
            'name': name
        }
        self.response = requests.post(
            "http://memesapi.course.qa-practice.com/authorize",
            json=body
        )
        self.response_json = self.response.json()

        return self.response_json['token']





