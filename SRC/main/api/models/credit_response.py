from pydantic import BaseModel


class CreditResponse(BaseModel):
    id: int
    amount: int
    termMonths: int
    balance: int
    creditId: int