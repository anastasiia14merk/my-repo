import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class GetAllPictures(BaseEndpoint):
    def get_all_pictures(self, token):
        headers = {"Authorization": token}

        self.response = requests.get(
            f"{BASE_URL}/meme", headers=headers, timeout=REQUEST_TIMEOUT
        )

    def check_get_all_pictures(self):
        assert self.json is not None
        assert "data" in self.json
