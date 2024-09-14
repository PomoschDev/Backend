from pydantic import BaseModel, UUID4, ConfigDict


class NaturalUserSchema(BaseModel):
    id: UUID4
    user_id: UUID4
    name: str
    phone: str
    address: str
    card_number: str

    model_config = ConfigDict(from_attributes=True)
