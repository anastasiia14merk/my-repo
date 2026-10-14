import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class DeleteOnePicture(BaseEndpoint):
    def delete_one_picture(self, token, picture_id):
        headers = {"Authorization": token}
        self.response = requests.delete(
            f"{BASE_URL}/meme/{picture_id}", headers=headers, timeout=REQUEST_TIMEOUT
        )
