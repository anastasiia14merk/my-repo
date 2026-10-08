import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteOnePicture(BaseEndpoint):
    def delete_one_picture(self, token, picture_id):
        headers = {"Authorization": token}
        self.response = requests.delete(
            f"http://memesapi.course.qa-practice.com/meme/{picture_id}", headers=headers
        )
