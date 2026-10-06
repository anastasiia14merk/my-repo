import pytest

from endpoints.post_authorise import PostAuthorise
from endpoints.get_autorise import CheckAuthorise
from endpoints.get_all_pictures import GetAllPictures
from endpoints.get_one_picture import GetOnePicture
from endpoints.post_one_picture import PostOnePicture
from endpoints.put_one_picture import PutOnePicture
from endpoints.delete_one_picture import DeleteOnePicture



@pytest.fixture
def token():
    endpoint = PostAuthorise()
    token = endpoint.authorise('Anastasiia')
    return token

@pytest.fixture
def check_authorise_endpoint():
    return CheckAuthorise()

@pytest.fixture
def get_all_pictures_endpoint():
    return GetAllPictures()

@pytest.fixture
def get_one_picture_endpoint():
    return GetOnePicture()

@pytest.fixture
def post_one_picture_endpoint():
    return PostOnePicture()

@pytest.fixture
def put_one_picture_endpoint():
    return PutOnePicture()

@pytest.fixture
def delete_one_picture_endpoint():
    return DeleteOnePicture()
