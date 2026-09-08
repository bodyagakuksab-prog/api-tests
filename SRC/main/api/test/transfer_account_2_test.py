import pytest
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.db.crud.account_crud import AccountCrudDb as Account, AccountCrudDb
from  sqlalchemy.orm import Session

@pytest.mark.api
class TestDepositAccount:
    def test_transfer_account(
            self,
            api_manager: ApiManager,
            create_user_request:CreateUserRequest,
            db_session: Session
    ):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0

        account_id = response.id
        deposit_response = api_manager.user_steps.deposit_account(
            create_user_request,
            account_id,
            1000
        )
        assert deposit_response.balance == 1000

        second_response = api_manager.user_steps.create_account(create_user_request)
        assert second_response.balance == 0
        second_account_id = second_response.id

        transfer_response = api_manager.user_steps.transfer_account(
            create_user_request,
            account_id,
            second_account_id,
            500
        )
        assert transfer_response.fromAccountId == account_id
        assert transfer_response.toAccountId == second_account_id
        assert transfer_response.fromAccountIdBalance == 500

        first_account_from_db = Account.get_account_by_id(
            db_session,
            account_id
        )

        second_account_from_db = Account.get_account_by_id(
            db_session,
            second_account_id
        )
        assert first_account_from_db.balance == 500
        assert second_account_from_db.balance == 500

    def test_transfer_account_invalid(
            self,
            api_manager: ApiManager,
            create_user_request:CreateUserRequest,
            db_session: Session
    ):

        from_account = api_manager.user_steps.create_account(create_user_request)
        to_account = api_manager.user_steps.create_account(create_user_request)

        from_account_id = from_account.id
        to_account_id = to_account.id

        api_manager.user_steps.deposit_account(
            create_user_request,
            from_account_id,
            1000
        )
        api_manager.user_steps.transfer_invalid_account(
            create_user_request,
            from_account_id,
            to_account_id,
            2000
        )
        from_account_from_db = Account.get_account_by_id(
            db_session,
            from_account_id
        )
        to_account_from_db = Account.get_account_by_id(
            db_session,
            to_account_id
        )
        assert from_account_from_db.balance == 1000
        assert to_account_from_db.balance == 0
