# import allure
#
# import pytest

# @allure.epic("Memes API")
# @allure.feature("Check authorise")
# @allure.title("Check authorise after creating token")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_check_authorise(check_authorise_endpoint, token):
#     check_authorise_endpoint.check_authorise(token)
#     check_authorise_endpoint.check_status_code(200)
#     assert 'Token is alive' in check_authorise_endpoint.response.text


# @allure.epic("Memes API")
# @allure.feature("Get all pictures")
# @allure.title("Check getting all pictures")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_get_all_pictures(get_all_pictures_endpoint, token):
#     get_all_pictures_endpoint.get_all_pictures(token)
#     get_all_pictures_endpoint.check_status_code(200)
#     response_json = get_all_pictures_endpoint.json
#     assert response_json is not None
#     assert "data" in response_json

# @allure.epic("Memes API")
# @allure.feature("Get one picture")
# @allure.title("Check getting one picture")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_get_one_picture(get_one_picture_endpoint, token):
#     picture_id = 1
#     get_one_picture_endpoint.get_one_picture(token, picture_id)
#     get_one_picture_endpoint.check_status_code(200)
#     response_json = get_one_picture_endpoint.json
#     assert response_json["id"] == picture_id
#     assert "info" in response_json
#     assert "tags" in response_json
#     assert "text" in response_json
#     assert "updated_by" in response_json
#     assert "url" in response_json


# @allure.epic("Memes API")
# @allure.feature("Post one picture with correct data")
# @allure.title("Check creating one picture with correct data")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_post_one_picture(post_one_picture_endpoint, token):
#     body = {
#         "text": "Funny meme",
#         "url": "https://example.com/meme.jpg",
#         "tags": ["funny", "meme"],
#         "info": {
#             "type": "image"
#        }
#     }
#     post_one_picture_endpoint.post_one_picture(token, body)
#     post_one_picture_endpoint.check_status_code(200)
#     response_json = post_one_picture_endpoint.json
#     assert "id" in response_json
#     assert response_json["text"] == body["text"]
#     assert response_json["url"] == body["url"]
#     assert response_json["tags"] == body["tags"]
#     assert response_json["info"] == body["info"]
#
#
# @pytest.mark.parametrize("missing_field", [
#     "text",
#     "url",
#     "tags",
#     "info"
# ])
#
# @allure.epic("Memes API")
# @allure.feature("Post one picture with missing data")
# @allure.title("Check creating one picture with missing data")
# @allure.severity(allure.severity_level.NORMAL)
# def test_post_one_picture_missing_field(post_one_picture_endpoint, token, missing_field):
#     body = {
#         "text": "Funny meme",
#         "url": "https://example.com/meme.jpg",
#         "tags": ["funny", "meme"],
#         "info": {
#             "type": "image"
#         }
#     }
#     body.pop(missing_field)
#     post_one_picture_endpoint.post_one_picture(token, body)
#     post_one_picture_endpoint.check_status_code(400)
#

# @allure.epic("Memes API")
# @allure.feature("Put one picture with correct data")
# @allure.title("Check updating one picture with correct data")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_put_one_picture(post_one_picture_endpoint, put_one_picture_endpoint, token):
#     created_body = {
#         "text": "Funny  old meme",
#         "url": "https://oldexample.com/meme.jpg",
#         "tags": ["funny", "meme", "old"],
#         "info": {
#             "type": "old image"
#         }
#     }
#     post_one_picture_endpoint.post_one_picture(token, created_body),
#     post_one_picture_endpoint.check_status_code(200)
#     picture_id = post_one_picture_endpoint.json["id"]
#
#     new_body = {
#         "id": picture_id,
#         "text": "Funny  new meme",
#         "url": "https://newexample.com/meme.jpg",
#         "tags": ["funny", "meme", "new"],
#         "info": {
#             "type": "new image"
#         }
#     }
#
#     put_one_picture_endpoint.put_one_picture(token, picture_id, new_body)
#     response_json = put_one_picture_endpoint.json
#     put_one_picture_endpoint.check_status_code(200)
#
#     assert response_json["text"] == new_body["text"]
#     assert response_json["url"] == new_body["url"]
#     assert response_json["tags"] == new_body["tags"]
#     assert response_json["info"] == new_body["info"]
#     assert int(response_json["id"]) == picture_id
#
#
# @pytest.mark.parametrize("missing_field",[
#     "id",
#     "text",
#     "url",
#     "tags",
#     "info"
# ])
#
#
# @allure.epic("Memes API")
# @allure.feature("Put one picture with missing data")
# @allure.title("Check updating one picture with missing data")
# @allure.severity(allure.severity_level.NORMAL)
# def test_put_one_picture_missing_field(post_one_picture_endpoint,
#                                        put_one_picture_endpoint,
#                                        token,
#                                        missing_field):
#     created_body = {
#         "text": "Funny  old meme",
#         "url": "https://oldexample.com/meme.jpg",
#         "tags": ["funny", "meme", "old"],
#         "info": {
#             "type": "old image"
#         }
#     }
#     post_one_picture_endpoint.post_one_picture(token, created_body),
#     post_one_picture_endpoint.check_status_code(200)
#     picture_id = post_one_picture_endpoint.json["id"]
#
#     new_body = {
#         "id": picture_id,
#         "text": "Funny  new new meme",
#         "url": "https://newnewexample.com/meme.jpg",
#         "tags": ["funny", "meme", "new","new"],
#         "info": {
#             "type": "new new image"
#         }
#     }
#     new_body.pop(missing_field)
#     put_one_picture_endpoint.put_one_picture(token, picture_id, new_body)
#     put_one_picture_endpoint.check_status_code(400)


# @allure.epic("Memes API")
# @allure.feature("Delete one picture")
# @allure.title("Check deleting one picture")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_delete_one_picture(post_one_picture_endpoint, delete_one_picture_endpoint, token):
#     created_body = {
#         "text": "Funny  old meme",
#         "url": "https://oldexample.com/meme.jpg",
#         "tags": ["funny", "meme", "old"],
#         "info": {
#             "type": "old image"
#         }
#     }
#     post_one_picture_endpoint.post_one_picture(token, created_body),
#     post_one_picture_endpoint.check_status_code(200)
#     picture_id = post_one_picture_endpoint.json["id"]
#     delete_one_picture_endpoint.delete_one_picture(token, picture_id)
#     delete_one_picture_endpoint.check_status_code(200)
