import allure


@allure.epic("Memes API")
@allure.feature("Delete one picture")
@allure.title("Check deleting one picture")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_one_picture(picture_id_for_delete, delete_one_picture_endpoint, token):
    delete_one_picture_endpoint.delete_one_picture(token, picture_id_for_delete)
    delete_one_picture_endpoint.check_status_code(200)
