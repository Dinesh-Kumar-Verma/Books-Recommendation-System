import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create timestamped log file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"app_{timestamp}.log"
log_file_path = os.path.join(LOG_DIR, log_file)

# --- Configure logging globally ---
logging.basicConfig(
    level=logging.INFO,   # INFO and above
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

