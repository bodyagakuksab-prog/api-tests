from pydantic import BaseModel

class TransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: int