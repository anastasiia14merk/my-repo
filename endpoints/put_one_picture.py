import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class PutOnePicture(BaseEndpoint):
    def put_one_picture(self, token, picture_id, body):
        headers = {"Authorization": token}
        self.response = requests.put(
            f"{BASE_URL}/meme/{picture_id}",
            headers=headers,
            json=body,
            timeout=REQUEST_TIMEOUT,
        )
