import allure


@allure.epic("Memes API")
@allure.feature("Get one picture")
@allure.title("Check getting one picture")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_one_picture(get_one_picture_endpoint,created_picture_id, token):
    picture_id = created_picture_id
    get_one_picture_endpoint.get_one_picture(token, picture_id)
    get_one_picture_endpoint.check_status_code(200)
    get_one_picture_endpoint.check_get_one_picture(picture_id)


@allure.epic("Memes API")
@allure.feature("Get one picture")
@allure.title("Check getting one picture with deleted id")
@allure.severity(allure.severity_level.NORMAL)
def test_get_one_picture_with_deleted_id(get_one_picture_endpoint, deleted_picture_id, token):
    get_one_picture_endpoint.get_one_picture(token, deleted_picture_id)
    get_one_picture_endpoint.check_status_code(404)
