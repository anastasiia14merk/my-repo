import requests

from endpoints.base_endpoint import BaseEndpoint

class PostOnePicture(BaseEndpoint):
    def post_one_picture(self, token, body):
        headers = {
            "Authorization":token
        }

        self.response = requests.post(
        "http://memesapi.course.qa-practice.com/meme",
        headers=headers,
        json=body
        )

    def check_created_picture(self, body):
        assert "id" in self.json
        assert self.json["text"] == body["text"]
        assert self.json["url"] == body["url"]
        assert self.json["tags"] == body["tags"]
        assert self.json["info"] == body["info"]

