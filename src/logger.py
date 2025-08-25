import logging
from datetime import datetime
import os
import sys

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOGS_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(module)s - %(lineno)d - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOGS_FILE_PATH), logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('mlproject')
