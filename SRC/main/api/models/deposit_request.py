from SRC.main.api.models.base_modul import BaseModel

class DepositRequest(BaseModel):
    accountId: int
    amount: int