import requests
from pydantic import BaseModel
from SRC.main.api.requests.requester import Requester
from SRC.main.api.models.transfer_response import TransferResponse
class TransferAccountRequester(Requester):
    def post(self, model:BaseModel)->TransferResponse:
        url=f"{self.base_url}/account/transfer"
        response=requests.post(
            url=url,
            headers=self.headers,
            json=model.model_dump()
        )

        self.response_spec(response)
        return TransferResponse(**response.json())