import requests

from endpoints.base_endpoint import BaseEndpoint

class GetAllPictures(BaseEndpoint):
    def get_all_pictures(self,token):
        headers = {
            "Authorization": token
        }

        self.response = requests.get(
        "http://memesapi.course.qa-practice.com/meme",
        headers=headers
        )

