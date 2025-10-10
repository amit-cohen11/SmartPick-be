from logger import logger
import uvicorn
from typing import Dict
from fastapi import FastAPI


app = FastAPI()

logger.debug("Starting FastAPI server1...", extra={"newKey": "newValue", "anotherKey": 12345})


@app.post("/echo_number")
async def echo_number(input: int):
    logger.debug("", extra={"number": input})
    try:
        a = 1/0
    except Exception:
        logger.debug("Something went wrong", exc_info=True, extra={"number": input})
    return {"number": input}


if __name__ == "__main__":
    logger.info("Starting FastAPI server2...")
    uvicorn.run("app:app", host="localhost", port=8005, reload=True)
