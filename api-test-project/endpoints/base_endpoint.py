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

    def check_picture(self, body=None, picture_id=None):
        data = self.json
        assert "id" in data, "Response is missing field: id"
        if picture_id is not None:
            assert int(data["id"]) == int(picture_id), "Unexpected meme ID"

        for field in ("text", "url", "tags", "info"):
            assert field in data, f"Response is missing field: {field}"
            if body is not None:
                assert data[field] == body[field], f"Unexpected value for field: {field}"
