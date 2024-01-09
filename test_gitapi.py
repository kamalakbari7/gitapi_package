import pytest
from gitapi_pkg import gitapi


def test_api_token_name():
    with pytest.raises(ValueError):
        gitapi.github_user_info(10)




