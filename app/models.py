from sqlalchemy import Column, Integer, String
from app.database import Base

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100),nullable=False)
    ip_address = Column(String(50), nullable=False)
    operating_system = Column(String(100), nullable=False)
    environment = Column(String(50), nullable=False)
