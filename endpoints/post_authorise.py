import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class PostAuthorise(BaseEndpoint):
    def post_authorise(self, body):
        self.response = requests.post(
            f"{BASE_URL}/authorize", json=body, timeout=REQUEST_TIMEOUT
        )

    def authorise(self, name):
        self.post_authorise({"name": name})
        status = self.response.status_code
        if status != 200:
            raise RuntimeError(
                f"Failed to obtain authorization token during setup. "
                f"Expected HTTP 200, got {status}"
            )

        try:
            payload = self.json
        except requests.exceptions.JSONDecodeError:
            raise RuntimeError(
                "Failed to obtain authorization token during setup: "
                "response is not valid JSON"
            ) from None
        if (
            not isinstance(payload, dict)
            or not isinstance(payload.get("token"), str)
            or not payload["token"]
        ):
            raise RuntimeError(
                "Failed to obtain authorization token during setup: "
                "response must contain a non-empty token"
            )
        return payload["token"]
