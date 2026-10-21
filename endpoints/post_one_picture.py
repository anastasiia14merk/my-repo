import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class PostOnePicture(BaseEndpoint):
    def __init__(self, on_created=None):
        super().__init__()
        self.on_created = on_created

    def post_one_picture(self, token, body):
        headers = {"Authorization": token}

        self.response = requests.post(
            f"{BASE_URL}/meme", headers=headers, json=body, timeout=REQUEST_TIMEOUT
        )

        # Register cleanup before the test checks status or response fields.
        if self.on_created is not None:
            try:
                payload = self.json
            except requests.exceptions.JSONDecodeError:
                return
            if isinstance(payload, dict) and payload.get("id") is not None:
                self.on_created(token, payload["id"])
