import requests

from config import BASE_URL, REQUEST_TIMEOUT
from endpoints.base_endpoint import BaseEndpoint


class CheckAuthorise(BaseEndpoint):
    def check_authorise(self, token):
        try:
            self.response = requests.get(
                f"{BASE_URL}/authorize/{token}", timeout=REQUEST_TIMEOUT
            )
        except requests.exceptions.RequestException:
            # requests exceptions can include the token-bearing URL.
            raise RuntimeError(
                "Token validation request failed (network or timeout)"
            ) from None

    def check_token_is_alive(self):
        assert "Token is alive" in self.response.text
