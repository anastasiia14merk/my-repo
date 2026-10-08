import requests

from endpoints.base_endpoint import BaseEndpoint

class CheckAuthorise(BaseEndpoint):
    def check_authorise(self, token):
        self.response = requests.get(
            f'http://memesapi.course.qa-practice.com/authorize/{token}',
        )
        print(self.response.text)

    def check_token_is_alive(self):
        assert 'Token is alive' in self.response.text



