from SRC.main.api.models.base_modul import BaseModel

class User(BaseModel):
    username: str
    role: str


class LoginUserResponse(BaseModel):
    token: str
    user: User