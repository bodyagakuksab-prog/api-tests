import pytest
from sqlalchemy.orm import Session

from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from SRC.main.api.models.create_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditAccount:

    def test_credit_account(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session
    ):
        account = api_manager.user_steps.create_account(credit_user_request)

        response = api_manager.user_steps.credit_account(
            credit_user_request,
            account.id,
            5000,
            12
        )
        assert response.id == account.id
        assert response.amount == 5000
        assert response.termMonths == 12
        assert response.creditId is not None

        credit_from_db = Credit.get_credit_by_account_id(
            db_session,
            account.id
        )
        assert credit_from_db is not None
        assert credit_from_db.amount == 5000
        assert credit_from_db.term_months == 12
        assert credit_from_db.account_id == account.id

    def test_credit_account_invalid(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session
    ):
        account = api_manager.user_steps.create_account(credit_user_request)

        api_manager.user_steps.credit_invalid_account(
            credit_user_request,
            account.id,
            -1000,
            12
        )
        credit_from_db = Credit.get_credit_by_account_id(
            db_session,
            account.id
        )
        assert credit_from_db is None
