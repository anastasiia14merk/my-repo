class BaseEndpoint:
    def __init__(self):
        self.response = None

    @property
    def json(self):
        return self.response.json()

    def check_status_code(self, code):
        assert self.response is not None, "No HTTP response: send a request first"
        actual = self.response.status_code
        method = self.response.request.method
        # Do not include URLs, headers or bodies: they may contain a token.
        assert actual == code, (
            f"{type(self).__name__} ({method}): expected HTTP {code}, got {actual}"
        )
