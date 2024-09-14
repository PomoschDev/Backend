from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from src.app.schemas.user.user_role import UserRole


class UserSchema(BaseModel):
    email: str
    password: str
    username: str
    role: UserRole
    company: bool
    status: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
