from uuid import uuid4

import allure
import pytest


@allure.epic("Memes API")
@allure.feature("Check authorise")
@allure.title("Check authorise after creating token")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_authorise(check_authorise_endpoint, token):
    check_authorise_endpoint.check_authorise(token)
    check_authorise_endpoint.check_status_code(200)
    check_authorise_endpoint.check_token_is_alive()


@pytest.mark.parametrize(
    "body",
    [
        pytest.param({}, id="missing-name"),
        pytest.param({"name": 123}, id="integer-name"),
        pytest.param({"name": None}, id="null-name"),
        pytest.param({"name": []}, id="list-name"),
        pytest.param({"name": {}}, id="object-name"),
    ],
)
@allure.epic("Memes API")
@allure.feature("Create authorization token")
@allure.title("Reject authorization with invalid name")
@allure.severity(allure.severity_level.NORMAL)
def test_authorise_with_invalid_name(post_authorise_endpoint, body):
    post_authorise_endpoint.post_authorise(body)
    post_authorise_endpoint.check_status_code(400)
    assert "Invalid parameters" in post_authorise_endpoint.response.text


@allure.epic("Memes API")
@allure.feature("Check authorise")
@allure.title("Reject a nonexistent authorization token")
@allure.severity(allure.severity_level.NORMAL)
def test_check_authorise_with_nonexistent_token(check_authorise_endpoint):
    nonexistent_token = uuid4().hex
    check_authorise_endpoint.check_authorise(nonexistent_token)
    check_authorise_endpoint.check_status_code(404)
    assert "Token not found" in check_authorise_endpoint.response.text
