from http import HTTPStatus
import requests

from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.models.create_user_response import CreateUserResponse
from SRC.main.api.requests.requester import Requester


class CreateUserRequester(Requester):
    def post(self, create_user_request: CreateUserRequest):
        url=f"{self.base_url}/admin/create"
        response = requests.post(
            url=url,
            json=create_user_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
            return CreateUserResponse(**response.json())
        return response