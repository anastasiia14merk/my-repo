import allure


@allure.epic("Memes API")
@allure.feature("Get one picture")
@allure.title("Check getting one picture")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_one_picture(get_one_picture_endpoint, token):
    picture_id = 1
    get_one_picture_endpoint.get_one_picture(token, picture_id)
    get_one_picture_endpoint.check_status_code(200)
    response_json = get_one_picture_endpoint.json
    assert response_json["id"] == picture_id
    assert "info" in response_json
    assert "tags" in response_json
    assert "text" in response_json
    assert "updated_by" in response_json
    assert "url" in response_json
