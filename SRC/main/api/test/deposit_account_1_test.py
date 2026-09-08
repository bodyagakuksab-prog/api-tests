import pytest
from sqlalchemy.orm import Session

from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Account, AccountCrudDb
from SRC.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0

        account_id = response.id
        deposit_response = api_manager.user_steps.deposit_account(
            create_user_request,
            account_id,
            1000
        )
        assert deposit_response.balance == 1000

        account_from_db =Account.get_account_by_id(db_session, account_id)
        assert account_from_db.balance == 1000



    def test_deposit_account_invalid(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_request)
        account_id = response.id
        api_manager.user_steps.deposit_invalid_account(
            create_user_request,
            account_id,
            -1000
        )
        account_from_db =Account.get_account_by_id(db_session, account_id)
        assert account_from_db.balance == 0



