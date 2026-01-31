from fastapi import FastAPI, Request
from app.api.v1.api import api_router
import logging
import time

# 1. Setup Logging
logging.basicConfig(
    filename='/var/log/app/fastapi.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)
logger = logging.getLogger("api")

app = FastAPI(title="AWS ELK Lab")

# 2. Add Middleware to log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = round(time.time() - start_time, 4)
    
    # This line is what actually WRITES to the file
    logger.info(f"{request.method} | {request.url.path} | {response.status_code} | {duration}")
    
    return response

app.include_router(api_router, prefix="/api/v1")