from pydantic import BaseModel

class TransferResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance:  float