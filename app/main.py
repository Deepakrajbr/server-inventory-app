from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base, Server
from app.schemas import ServerCreate
from app.schemas import ServerCreate, ServerUpdate

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Server Inventory API Running"
    }

@app.post("/servers")
def create_server(
    server: ServerCreate,
    db: Session = Depends(get_db)
):

    new_server = Server(
        name=server.name,
        ip_address=server.ip_address,
        operating_system=server.operating_system,
        environment=server.environment
    )

    db.add(new_server)
    db.commit()
    db.refresh(new_server)

    return {
        "message": "Server added successfully",
        "id": new_server.id
    }
@app.get("/servers")
def get_servers(db: Session = Depends(get_db)):
    servers = db.query(Server).all()

    return servers
@app.get("/servers/{server_id}")
def get_server(server_id: int, db: Session = Depends(get_db)):

    server = db.query(Server).filter(
        Server.id == server_id
    ).first()

    if not server:
        return {
            "message": "Server not found"
        }

    return server

@app.put("/servers/{server_id}")
def update_server(
    server_id: int,
    updated_server: ServerUpdate,
    db: Session = Depends(get_db)
):

    server = db.query(Server).filter(
        Server.id == server_id
    ).first()

    if not server:
        return {
            "message": "Server not found"
        }

    server.name = updated_server.name
    server.ip_address = updated_server.ip_address
    server.operating_system = updated_server.operating_system
    server.environment = updated_server.environment

    db.commit()

    return {
        "message": "Server updated successfully"
    }

@app.delete("/servers/{server_id}")
def delete_server(
    server_id: int,
    db: Session = Depends(get_db)
):

    server = db.query(Server).filter(
        Server.id == server_id
    ).first()

    if not server:
        return {
            "message": "Server not found"
        }

    db.delete(server)
    db.commit()

    return {
        "message": "Server deleted successfully"
    }
