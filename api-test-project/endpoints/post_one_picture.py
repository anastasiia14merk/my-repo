import requests

from endpoints.base_endpoint import BaseEndpoint

class PostOnePicture(BaseEndpoint):
    def post_one_picture(self, token, body):
        headers = {
            "Authorization":token
        }

        self.response = requests.post(
        "http://memesapi.course.qa-practice.com/meme",
        headers=headers,
        json=body
        )
