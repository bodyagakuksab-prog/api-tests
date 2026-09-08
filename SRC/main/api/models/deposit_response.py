from SRC.main.api.models.base_modul import BaseModel

class DepositResponse(BaseModel):
    id: int
    balance: int