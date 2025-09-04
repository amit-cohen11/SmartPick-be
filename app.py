from fastapi import FastAPI
from typing import Dict
import logging
import uvicorn
import json

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

logging.info("Starting FastAPI server1...")

def log_to_file(data: Dict):
    logging.info(str(data))

@app.post("/echo_json")
async def echo_json(data: Dict):
    log_to_file(data)
    return data

@app.post("/echo_number")
async def echo_number(input: int):
    log_to_file({"number": input})
    return {"number": input}

if __name__ == "__main__":
    logging.info("Starting FastAPI server2...")
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
