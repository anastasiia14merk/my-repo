import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class PostAuthorise(BaseEndpoint):
    def authorise(self, name):
        body = {"name": name}
        self.response = requests.post(
            f"{BASE_URL}/authorize", json=body, timeout=REQUEST_TIMEOUT
        )
        self.check_status_code(200)
        try:
            payload = self.json
        except requests.exceptions.JSONDecodeError:
            raise AssertionError("Authorization response is not valid JSON") from None
        if (
            not isinstance(payload, dict)
            or not isinstance(payload.get("token"), str)
            or not payload["token"]
        ):
            raise AssertionError(
                "Authorization response must contain a non-empty token"
            )
        return payload["token"]
