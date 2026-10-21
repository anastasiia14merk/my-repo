import allure
import pytest

import requests

from config import BASE_URL, REQUEST_TIMEOUT

@pytest.mark.parametrize(
    "headers",
    [
        pytest.param({}, id="without-token"),
        pytest.param(
            {"Authorization": "invalid-token"},
            id="invalid-token",
        ),
    ],
)
@allure.epic("Memes API")
@allure.feature("Access without authorization")
@allure.title("Reject getting memes without valid authorization")
def test_get_all_pictures_without_valid_authorization(headers):
    response = requests.get(
        f"{BASE_URL}/meme",
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 401, (
        f"Expected HTTP 401, got {response.status_code}"
    )