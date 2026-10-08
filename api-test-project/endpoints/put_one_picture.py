import requests

from endpoints.base_endpoint import BaseEndpoint

class PutOnePicture(BaseEndpoint):
    def put_one_picture(self, token, picture_id, body):
        headers = {
            "Authorization":token
        }
        self.response = requests.put(
        f"http://memesapi.course.qa-practice.com/meme/{picture_id}",
        headers=headers,
        json=body
        )

    def check_put_one_picture(self, picture_id, body):
        assert int(self.json["id"]) == picture_id
        assert self.json["text"] == body["text"]
        assert self.json["url"] == body["url"]
        assert self.json["tags"] == body["tags"]
        assert self.json["info"] == body["info"]
