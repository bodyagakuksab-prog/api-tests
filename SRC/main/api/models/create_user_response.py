from SRC.main.api.models.base_modul import BaseModel

class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str