import pytest

from endpoints.post_authorise import PostAuthorise
from endpoints.get_autorise import CheckAuthorise
from endpoints.get_all_pictures import GetAllPictures
from endpoints.get_one_picture import GetOnePicture
from endpoints.post_one_picture import PostOnePicture
from endpoints.put_one_picture import PutOnePicture
from endpoints.delete_one_picture import DeleteOnePicture


@pytest.fixture(scope="session")
def token(request):
    saved_token = request.config.cache.get('memes_api/token', None)

    if saved_token:
        print("Saved token found")
        check_endpoint = CheckAuthorise()
        check_endpoint.check_authorise(saved_token)

        if (
            check_endpoint.response.status_code == 200
            and 'Token is alive' in check_endpoint.response.text
        ):
            print("Saved token is alive")
            return saved_token

    print("Creating new token")
    endpoint = PostAuthorise()
    new_token = endpoint.authorise('Anastasiia')
    request.config.cache.set('memes_api/token', new_token)
    return new_token


@pytest.fixture
def check_authorise_endpoint():
    return CheckAuthorise()

@pytest.fixture
def created_picture_id(post_one_picture_endpoint, token, delete_one_picture_endpoint):
    body = {
        "text": "Funny meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "meme"],
        "info": {
            "type": "image"
        }
    }

    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(200)

    created_picture_id = post_one_picture_endpoint.json["id"]

    yield created_picture_id

    delete_one_picture_endpoint.delete_one_picture(token, created_picture_id)

@pytest.fixture
def get_all_pictures_endpoint():
    return GetAllPictures()

@pytest.fixture
def get_one_picture_endpoint():
    return GetOnePicture()

@pytest.fixture
def deleted_picture_id(
        post_one_picture_endpoint,
        token,
        delete_one_picture_endpoint
):
    body = {
        "text": "Funny meme",
        "url": "https://example.com/meme.jpg",
        "tags": ["funny", "meme"],
        "info": {
            "type": "image"
        }
    }
    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(200)
    picture_id = post_one_picture_endpoint.json["id"]

    delete_one_picture_endpoint.delete_one_picture(token, picture_id)
    delete_one_picture_endpoint.check_status_code(200)
    return picture_id


@pytest.fixture
def post_one_picture_endpoint():
    return PostOnePicture()

@pytest.fixture
def put_one_picture_endpoint():
    return PutOnePicture()

@pytest.fixture
def delete_one_picture_endpoint():
    return DeleteOnePicture()

@pytest.fixture
def picture_id_for_delete(post_one_picture_endpoint, token):
    body = {
        "text": "Funny old meme",
        "url": "https://oldexample.com/meme.jpg",
        "tags": ["funny", "meme", "old"],
        "info": {
            "type": "old image"
        }
    }

    post_one_picture_endpoint.post_one_picture(token, body)
    post_one_picture_endpoint.check_status_code(200)

    return post_one_picture_endpoint.json["id"]
