from pydantic import BaseModel

class CreditRequest(BaseModel):
    accountId: int
    amount: int
    termMonths: int