import pytest
from sqlalchemy.orm import Session
from SRC.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from SRC.main.api.classes.api_manager import ApiManager
from SRC.main.api.models.create_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session,
    ):
        account = api_manager.user_steps.create_account(credit_user_request)

        response = api_manager.user_steps.credit_account(
            credit_user_request,
            account.id,
            5000,
            12
        )

        api_manager.user_steps.deposit_account(
            credit_user_request,
            account.id,
            5000
        )

        repay_response = api_manager.user_steps.credit_repay(
            credit_user_request,
            response.creditId,
            account.id,
            5000
        )
        assert repay_response.creditId == response.creditId
        assert repay_response.amountDeposited == 5000

        credit_from_db = Credit.get_credit_by_account_id(
            db_session,
            account.id
        )
        assert credit_from_db.balance == 0


    def test_credit_repay_invalid(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session,
    ):
        account = api_manager.user_steps.create_account(credit_user_request)

        response = api_manager.user_steps.credit_account(
            credit_user_request,
            account.id,
            5000,
            12
        )
        api_manager.user_steps.deposit_account(
            credit_user_request,
            account.id,
            5000,
        )

        api_manager.user_steps.credit_repay_invalid(
            credit_user_request,
            response.creditId,
            account.id,
            6000
        )

        credit_from_db = Credit.get_credit_by_account_id(
            db_session,
            account.id
        )
        assert credit_from_db.balance == -5000