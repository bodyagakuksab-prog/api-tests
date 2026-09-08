from pydantic import BaseModel

class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: int