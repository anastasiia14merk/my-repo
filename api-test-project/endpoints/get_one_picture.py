import requests

from endpoints.base_endpoint import BaseEndpoint

class GetOnePicture(BaseEndpoint):
    def get_one_picture(self, token, picture_id):
        headers = {
            "Authorization":token
        }
        self.response = requests.get(
            f"http://memesapi.course.qa-practice.com/meme/{picture_id}",
            headers=headers
        )