import allure

import pytest

@allure.epic("Memes API")
@allure.feature("Post one picture with correct data")
@allure.title("Check creating one picture with correct data")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_one_picture(post_one_picture_endpoint, token):
    body = {
        "text": "Funny meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "meme"],
        "info": {
            "type": "image"
       }
    }
    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(200)
    post_one_picture_endpoint.check_created_picture(body)


@pytest.mark.parametrize("missing_field", [
    "text",
    "url",
    "tags",
    "info"
])


@allure.epic("Memes API")
@allure.feature("Post one picture with missing data")
@allure.title("Check creating one picture with missing data")
@allure.severity(allure.severity_level.NORMAL)
def test_post_one_picture_missing_field(post_one_picture_endpoint, token, missing_field):
    body = {
        "text": "Funny meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "meme"],
        "info": {
            "type": "image"
        }
    }
    body.pop(missing_field)
    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(400)
