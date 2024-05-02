from lib import get_secrets_login
import pytest

@pytest.fixture(scope="session")
def secrets_login(): #from here we will go to library
    return get_secrets_login()