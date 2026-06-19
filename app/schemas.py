from pydantic import BaseModel

class ServerCreate(BaseModel):
    name: str
    ip_address: str
    operating_system: str
    environment: str

class ServerUpdate(BaseModel):
    name: str
    ip_address: str
    operating_system: str
    environment: str
