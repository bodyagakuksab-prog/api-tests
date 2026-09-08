import allure

from SRC.main.api.foundation.endpoint import Endpoint
from SRC.main.api.foundation.requesters.crud_requester import CrudRequester
from SRC.main.api.foundation.requesters.validated_crud_requester import ValidatedCrudRequester
from SRC.main.api.models import create_user_request
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.credit_repay_request import CreditRepayRequest
from SRC.main.api.models.deposit_request import DepositRequest
from SRC.main.api.models.credit_request import CreditRequest
from SRC.main.api.models.transfer_request import TransferRequest
from SRC.main.api.specs.request_specs import RequestSpecs
from SRC.main.api.specs.response_specs import ResponseSpecs
from SRC.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidatedCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    @allure.step("Пополнение банковского счета")
    def deposit_account(self, create_user_request: CreateUserRequest, account_id: int, amount: int):
        deposit_request = DepositRequest(
            accountId = account_id,
            amount = amount
        )
        response = ValidatedCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response

    @allure.step("Неккоректное пополнение банковского счета")
    def deposit_invalid_account(
            self,
            create_user_request: CreateUserRequest,
            account_id: int,
            amount: int
    ):
        deposit_request = DepositRequest(
            accountId = account_id,
            amount = amount
        )
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_request)

    @allure.step("Перевод средств между банковскими счетами")
    def transfer_account(self, create_user_request: CreateUserRequest, from_account_id: int, to_account_id: int, amount: int):
        transfer_request = TransferRequest(
            fromAccountId=from_account_id,
            toAccountId=to_account_id,
            amount=amount
        )
        response = ValidatedCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response

    @allure.step("Некоректнный перевод средств между бфнковскими счетами")
    def transfer_invalid_account(
            self,
            create_user_request: CreateUserRequest,
            from_account_id: int,
            to_account_id: int,
            amount: int
    ):
        transfer_request = TransferRequest(
            fromAccountId=from_account_id,
            toAccountId=to_account_id,
            amount=amount
        )
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_unprocessable()
        ).post(transfer_request)

    @allure.step("Запрос на получение кредита")
    def credit_account(self, create_user_request: CreateUserRequest, account_id: int, amount: int, term_months: int):
        credit_request = CreditRequest(
            accountId = account_id,
            amount = amount,
            termMonths = term_months
        )
        response = ValidatedCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(credit_request)
        return response

    @allure.step("Некорректный запрос на получение кредита")
    def credit_invalid_account(
            self,
            create_user_request: CreateUserRequest,
            account_id: int,
            amount: int,
            term_months: int
    ):
        credit_request = CreditRequest(
            accountId = account_id,
            amount = amount,
            termMonths = term_months
    )
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(credit_request)

    @allure.step("Погашение кредита")
    def credit_repay(
            self,
            create_user_request: CreateUserRequest,
            credit_id: int,
            account_id: int,
            amount: int,
    ):
        credit_repay_request = CreditRepayRequest(
            creditId = credit_id,
            accountId = account_id,
            amount = amount
        )

        response = ValidatedCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_AMOUNT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response

    @allure.step("Некорректное погашение кредита")
    def credit_repay_invalid(
            self,
            create_user_request: CreateUserRequest,
            credit_id: int,
            account_id: int,
            amount: int,
    ):
        credit_repay_request = CreditRepayRequest(
            creditId=credit_id,
            accountId=account_id,
            amount=amount
        )
        CrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_AMOUNT_ACCOUNT,
            ResponseSpecs.request_unprocessable()
        ).post(credit_repay_request)





