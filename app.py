from fastapi import FastAPI
from typing import Dict
import logging
import uvicorn
import json

from database import engine
from models import Base
from models import User
from sqlalchemy.orm import Session
from database import SessionLocal

logging.info("Starting FastAPI server1...")

Base.metadata.create_all(bind=engine)

app = FastAPI()
logging.basicConfig(
    filename="/var/log/app/output.log",
    format=json.dumps({
        "timestamp": "%(asctime)s",
        "level": "%(levelname)s",
        "module": "%(module)s",
        "function": "%(funcName)s",
        "line": "%(lineno)d",
        "message": "%(message)s",
        "extra_info": "This is a placeholder for additional log context to ensure the log entry exceeds 64 bytes."
    }),
    level=logging.INFO
)

@app.get("/user")
def get_user():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return [user.__dict__ for user in users]

@app.post("/echo_json")
async def echo_json(data: Dict):
    logging.info(str(data))
    return data

@app.post("/echo_number")
async def echo_number(input: int):
    logging.info(str({"number": input}))
    return {"number": input}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
