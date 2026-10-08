import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllPictures(BaseEndpoint):
    def get_all_pictures(self, token):
        headers = {"Authorization": token}

        self.response = requests.get(
            "http://memesapi.course.qa-practice.com/meme", headers=headers
        )

    def check_get_all_pictures(self):
        assert self.json is not None
        assert "data" in self.json
