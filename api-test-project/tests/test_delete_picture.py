import allure


@allure.epic("Memes API")
@allure.feature("Delete one picture")
@allure.title("Check deleting one picture")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_one_picture(post_one_picture_endpoint, delete_one_picture_endpoint, token):
    created_body = {
        "text": "Funny  old meme",
        "url": "https://oldexample.com/meme.jpg",
        "tags": ["funny", "meme", "old"],
        "info": {
            "type": "old image"
        }
    }
    post_one_picture_endpoint.post_one_picture(token, created_body),
    post_one_picture_endpoint.check_status_code(200)
    picture_id = post_one_picture_endpoint.json["id"]
    delete_one_picture_endpoint.delete_one_picture(token, picture_id)
    delete_one_picture_endpoint.check_status_code(200)