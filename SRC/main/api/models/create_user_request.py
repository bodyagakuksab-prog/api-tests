from SRC.main.api.generators.creation_rule import CreationRule
from SRC.main.api.models.base_modul import BaseModel
from typing import Annotated

class CreateUserRequest(BaseModel):
    username: Annotated[str, CreationRule(regex=r"^[A-Za-z0-9]{3,15}$")]
    password: Annotated[str, CreationRule(regex=r"^[A-Z]{3}[a-z]{1}[0-9]{2}[!$_]{4}$")]
    role: Annotated[str, CreationRule(regex=r"^ROLE_USER")]

class CreditUserRequest(CreateUserRequest):
    role: Annotated[str, CreationRule(regex=r"^ROLE_CREDIT_SECRET")]
