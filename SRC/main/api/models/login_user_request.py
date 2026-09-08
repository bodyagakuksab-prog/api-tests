from SRC.main.api.models.base_modul import BaseModel

class LoginUserRequest(BaseModel):
    username: str
    password: str