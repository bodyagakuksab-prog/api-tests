import requests

from SRC.main.api.models.deposit_response import DepositResponse
from SRC.main.api.requests.requester import Requester


class DepositAccountRequester(Requester):
    def post(self, model=None)->DepositResponse:
        url = f"{self.base_url}/account/deposit"

        response = requests.post(
            url=url,
            headers=self.headers,
            json=model.model_dump()
        )

        self.response_spec(response)
        return DepositResponse(**response.json())