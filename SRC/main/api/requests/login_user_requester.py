from urllib import response
from requests import Response
from SRC.main.api.models.login_user_request import LoginUserRequest
from SRC.main.api.models.login_user_response import LoginUserResponse
from SRC.main.api.requests.requester import Requester
import requests


class  LoginUserRequester(Requester):
    def post(self, login_user_request: LoginUserRequest) -> LoginUserResponse | Response:
        url=f"{self.base_url}/auth/token/login"
        response = requests.post(
            url=url,
            json=login_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return LoginUserResponse(**response.json())


