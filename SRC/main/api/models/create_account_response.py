from SRC.main.api.models.base_modul import BaseModel


class CreateAccountResponse(BaseModel):
    id: int
    number: str
    balance: float