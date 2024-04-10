import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#saving my log file in paticular path
log_path = os.path.join(os.getcwd(),"logs")  # "logs" is file_name

os.makedirs(log_path,exist_ok=True)

# inside logs file created logs
LOG_FILEPATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)