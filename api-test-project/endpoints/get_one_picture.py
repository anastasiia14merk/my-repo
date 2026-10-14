import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class GetOnePicture(BaseEndpoint):
    def get_one_picture(self, token, picture_id):
        headers = {"Authorization": token}
        self.response = requests.get(
            f"{BASE_URL}/meme/{picture_id}", headers=headers, timeout=REQUEST_TIMEOUT
        )

    def check_get_one_picture(self, picture_id):
        assert int(self.json["id"]) == int(picture_id)
        assert "info" in self.json
        assert "tags" in self.json
        assert "text" in self.json
        assert "updated_by" in self.json
        assert "url" in self.json
