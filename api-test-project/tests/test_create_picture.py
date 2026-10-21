import allure
import pytest

from data import CREATE_MEME_BODY
from copy import deepcopy


@allure.epic("Memes API")
@allure.feature("Post one picture with correct data")
@allure.title("Check creating one picture with correct data")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_one_picture(post_one_picture_endpoint, token):
    body = deepcopy(CREATE_MEME_BODY)
    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(200)
    post_one_picture_endpoint.check_created_picture(body)


@pytest.mark.parametrize("missing_field", ["text", "url", "tags", "info"])
@allure.epic("Memes API")
@allure.feature("Post one picture with missing data")
@allure.title("Check creating one picture with missing data")
@allure.severity(allure.severity_level.NORMAL)
def test_post_one_picture_missing_field(
    post_one_picture_endpoint, token, missing_field
):
    body = deepcopy(CREATE_MEME_BODY)
    body.pop(missing_field)
    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(400)


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        pytest.param("text", ["Invalid text"], id="text-as-list"),
        pytest.param("url", ["https://example.com/meme.jpg"], id="url-as-list"),
        pytest.param("tags", "funny", id="tags-as-string"),
        pytest.param("info", ["image"], id="info-as-list"),
    ],
)
@allure.epic("Memes API")
@allure.feature("Post one picture with invalid field types")
@allure.title("Reject meme creation with an invalid field type")
@allure.severity(allure.severity_level.NORMAL)
def test_post_one_picture_invalid_field_type(
    post_one_picture_endpoint, token, field, invalid_value
):
    body = deepcopy(CREATE_MEME_BODY)
    body[field] = deepcopy(invalid_value)

    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(400)
