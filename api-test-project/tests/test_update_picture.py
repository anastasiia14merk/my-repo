import allure

import pytest

@allure.epic("Memes API")
@allure.feature("Put one picture with correct data")
@allure.title("Check updating one picture with correct data")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_one_picture(post_one_picture_endpoint, put_one_picture_endpoint, token):
    created_body = {
        "text": "Funny  old meme",
        "url": "https://oldexample.com/meme.jpg",
        "tags": ["funny", "meme", "old"],
        "info": {
            "type": "old image"
        }
    }
    post_one_picture_endpoint.post_one_picture(token, created_body),
    post_one_picture_endpoint.check_status_code(200)
    picture_id = post_one_picture_endpoint.json["id"]

    new_body = {
        "id": picture_id,
        "text": "Funny  new meme",
        "url": "https://newexample.com/meme.jpg",
        "tags": ["funny", "meme", "new"],
        "info": {
            "type": "new image"
        }
    }

    put_one_picture_endpoint.put_one_picture(token, picture_id, new_body)
    response_json = put_one_picture_endpoint.json
    put_one_picture_endpoint.check_status_code(200)

    assert response_json["text"] == new_body["text"]
    assert response_json["url"] == new_body["url"]
    assert response_json["tags"] == new_body["tags"]
    assert response_json["info"] == new_body["info"]
    assert int(response_json["id"]) == picture_id


@pytest.mark.parametrize("missing_field",[
    "id",
    "text",
    "url",
    "tags",
    "info"
])


@allure.epic("Memes API")
@allure.feature("Put one picture with missing data")
@allure.title("Check updating one picture with missing data")
@allure.severity(allure.severity_level.NORMAL)
def test_put_one_picture_missing_field(post_one_picture_endpoint,
                                       put_one_picture_endpoint,
                                       token,
                                       missing_field):
    created_body = {
        "text": "Funny  old meme",
        "url": "https://oldexample.com/meme.jpg",
        "tags": ["funny", "meme", "old"],
        "info": {
            "type": "old image"
        }
    }
    post_one_picture_endpoint.post_one_picture(token, created_body),
    post_one_picture_endpoint.check_status_code(200)
    picture_id = post_one_picture_endpoint.json["id"]

    new_body = {
        "id": picture_id,
        "text": "Funny  new new meme",
        "url": "https://newnewexample.com/meme.jpg",
        "tags": ["funny", "meme", "new","new"],
        "info": {
            "type": "new new image"
        }
    }
    new_body.pop(missing_field)
    put_one_picture_endpoint.put_one_picture(token, picture_id, new_body)
    put_one_picture_endpoint.check_status_code(400)
