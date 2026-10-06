import requests

from endpoints.base_endpoint import BaseEndpoint

class PutOnePicture(BaseEndpoint):
    def put_one_picture(self, token, picture_id, body):
        headers = {
            "Authorization":token
        }
        self.response = requests.put(
        f"http://memesapi.course.qa-practice.com/meme/{picture_id}",
        headers=headers,
        json=body
        )

