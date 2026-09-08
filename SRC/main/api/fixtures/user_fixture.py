import pytest

from SRC.main.api.fixtures.api_fixture import api_manager
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.models.create_user_request import CreateUserRequest, CreditUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request
@pytest.fixture
def credit_user_request(api_manager):
    credit_user_request = RandomModelGenerator.generate(CreditUserRequest)
    api_manager.admin_steps.create_user(credit_user_request)
    return credit_user_request