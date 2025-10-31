import logging
import os
from datetime import datetime

LOG_FILE = f"{os.getcwd()}/logs/{datetime.now().strftime('%Y_%m_%d')}.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
