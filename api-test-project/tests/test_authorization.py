import allure


@allure.epic("Memes API")
@allure.feature("Check authorise")
@allure.title("Check authorise after creating token")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_authorise(check_authorise_endpoint, token):
    check_authorise_endpoint.check_authorise(token)
    check_authorise_endpoint.check_status_code(200)
    assert 'Token is alive' in check_authorise_endpoint.response.text
