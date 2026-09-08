from enum import Enum
from SRC.main.api.models.base_modul import BaseModel
from typing import Optional, Type
from dataclasses import dataclass
from SRC.main.api.models.create_account_response import CreateAccountResponse
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_response import CreateUserResponse
from SRC.main.api.models.credit_repay_request import CreditRepayRequest
from SRC.main.api.models.credit_repay_response import CreditRepayResponse
from SRC.main.api.models.deposit_request import DepositRequest
from SRC.main.api.models.deposit_response import DepositResponse
from SRC.main.api.models.login_user_request import LoginUserRequest
from SRC.main.api.models.login_user_response import LoginUserResponse
from SRC.main.api.models.transfer_request import TransferRequest
from SRC.main.api.models.transfer_response import TransferResponse
from SRC.main.api.models.credit_request import CreditRequest
from SRC.main.api.models.credit_response import CreditResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url="/admin/create",
        response_model = CreateUserResponse,
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model = None,
        url= "/admin/users",
        response_model = None,
    )
    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequest,
        url= "/auth/token/login",
        response_model = LoginUserResponse,
    )
    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "/account/create",
        response_model = CreateAccountResponse
    )
    DEPOSIT_ACCOUNT = EndpointConfiguration(
        request_model = DepositRequest,
        url= "/account/deposit",
        response_model = DepositResponse
    )
    TRANSFER_ACCOUNT = EndpointConfiguration(
        request_model = TransferRequest,
        url= "/account/transfer",
        response_model = TransferResponse
    )
    CREDIT_ACCOUNT = EndpointConfiguration(
        request_model = CreditRequest,
        url= "/credit/request",
        response_model = CreditResponse
    )
    CREDIT_AMOUNT_ACCOUNT = EndpointConfiguration(
        request_model=CreditRepayRequest,
        url= "/credit/repay",
        response_model=CreditRepayResponse
    )