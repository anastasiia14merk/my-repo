import allure


@allure.epic("Memes API")
@allure.feature("Delete one picture")
@allure.title("Check deleting one picture")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_one_picture(
    picture_id_for_delete, delete_one_picture_endpoint, get_one_picture_endpoint, token
):
    delete_one_picture_endpoint.delete_one_picture(token, picture_id_for_delete)
    delete_one_picture_endpoint.check_status_code(200)
    get_one_picture_endpoint.get_one_picture(token, picture_id_for_delete)
    get_one_picture_endpoint.check_status_code(404)


@allure.epic("Memes API")
@allure.feature("Delete one picture")
@allure.title("Reject deletion of a nonexistent meme")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_one_picture_with_deleted_id(
    deleted_picture_id, delete_one_picture_endpoint, token
):
    delete_one_picture_endpoint.delete_one_picture(token, deleted_picture_id)
    delete_one_picture_endpoint.check_status_code(404)
