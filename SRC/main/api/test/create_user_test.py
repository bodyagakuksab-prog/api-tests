import pytest
from sqlalchemy.orm import Session
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.fixtures.api_fixture import api_manager
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.db.crud.user_crud import UserCrudDB as User



@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)],
    )
    def test_create_user_valid(self, api_manager: ApiManager ,create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, "Созданного пользователя нет в БД"

    @pytest.mark.parametrize(
        "username,password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abv!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0r"),
            ("Maxx4", "PASS!SW0RD"),
            ("Maxx5", "PASSSW0RD"),
            ("Maxx6", "PASS!SWRRd"),
        ]
    )
    def test_create_user_invalid(self, db_session: Session ,api_manager: ApiManager, username:str, password:str):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, " Пользователь создан, ошибка"