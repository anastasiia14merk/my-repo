import allure

@allure.epic("Memes API")
@allure.feature("Get all pictures")
@allure.title("Check getting all pictures")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_all_pictures(get_all_pictures_endpoint, token):
    get_all_pictures_endpoint.get_all_pictures(token)
    get_all_pictures_endpoint.check_status_code(200)
    get_all_pictures_endpoint.check_get_all_pictures()