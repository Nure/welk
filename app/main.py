from fastapi import FastAPI
from app.api.v1.api import api_router
import logging

# Log to the volume shared with Filebeat
logging.basicConfig(
    filename='/var/log/app/fastapi.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

app = FastAPI(title="AWS ELK Lab")
app.include_router(api_router, prefix="/api/v1")