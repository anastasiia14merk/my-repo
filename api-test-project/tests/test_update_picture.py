import allure
import pytest


@allure.epic("Memes API")
@allure.feature("Put one picture with correct data")
@allure.title("Check updating one picture with correct data")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_one_picture(put_one_picture_endpoint, token, created_picture_id):

    new_body = {
        "id": created_picture_id,
        "text": "Funny  new meme",
        "url": "https://newexample.com/meme.jpg",
        "tags": ["funny", "meme", "new"],
        "info": {"type": "new image"},
    }

    put_one_picture_endpoint.put_one_picture(token, created_picture_id, new_body)
    put_one_picture_endpoint.check_status_code(200)
    put_one_picture_endpoint.check_put_one_picture(created_picture_id, new_body)


@pytest.mark.parametrize("missing_field", ["id", "text", "url", "tags", "info"])
@allure.epic("Memes API")
@allure.feature("Put one picture with missing data")
@allure.title("Check updating one picture with missing data")
@allure.severity(allure.severity_level.NORMAL)
def test_put_one_picture_missing_field(
    created_picture_id, put_one_picture_endpoint, token, missing_field
):

    new_body = {
        "id": created_picture_id,
        "text": "Funny  new new meme",
        "url": "https://newnewexample.com/meme.jpg",
        "tags": ["funny", "meme", "new", "new"],
        "info": {"type": "new new image"},
    }
    new_body.pop(missing_field)
    put_one_picture_endpoint.put_one_picture(token, created_picture_id, new_body)
    put_one_picture_endpoint.check_status_code(400)
