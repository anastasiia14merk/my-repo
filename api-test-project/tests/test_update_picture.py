import allure
import pytest

from data import UPDATE_MEME_BODY
from copy import deepcopy


@allure.epic("Memes API")
@allure.feature("Put one picture with correct data")
@allure.title("Check updating one picture with correct data")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_one_picture(
    put_one_picture_endpoint, get_one_picture_endpoint, token, created_picture_id
):

    new_body = deepcopy(UPDATE_MEME_BODY)
    new_body["id"] = created_picture_id

    put_one_picture_endpoint.put_one_picture(token, created_picture_id, new_body)
    put_one_picture_endpoint.check_status_code(200)
    put_one_picture_endpoint.check_put_one_picture(created_picture_id, new_body)
    get_one_picture_endpoint.get_one_picture(token, created_picture_id)
    get_one_picture_endpoint.check_status_code(200)
    get_one_picture_endpoint.check_get_one_picture(created_picture_id)
    for field in ("text", "url", "tags", "info"):
        assert get_one_picture_endpoint.json[field] == new_body[field], field


@pytest.mark.parametrize("missing_field", ["id", "text", "url", "tags", "info"])
@allure.epic("Memes API")
@allure.feature("Put one picture with missing data")
@allure.title("Check updating one picture with missing data")
@allure.severity(allure.severity_level.NORMAL)
def test_put_one_picture_missing_field(
    created_picture_id, put_one_picture_endpoint, token, missing_field
):

    new_body = deepcopy(UPDATE_MEME_BODY)
    new_body["id"] = created_picture_id

    new_body.pop(missing_field)
    put_one_picture_endpoint.put_one_picture(token, created_picture_id, new_body)
    put_one_picture_endpoint.check_status_code(400)


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
@allure.feature("Put one picture with invalid field types")
@allure.title("Reject meme update with an invalid field type")
@allure.severity(allure.severity_level.NORMAL)
def test_put_one_picture_invalid_field_type(
    created_picture_id, put_one_picture_endpoint, token, field, invalid_value
):
    new_body = deepcopy(UPDATE_MEME_BODY)
    new_body["id"] = created_picture_id
    new_body[field] = deepcopy(invalid_value)

    put_one_picture_endpoint.put_one_picture(token, created_picture_id, new_body)
    put_one_picture_endpoint.check_status_code(400)
