import os
import sys
import logging

# Saves the current timestamp and data, which level is it from the root folder and which module you are running and lastly any kind of message you are adding
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Writes log files to a file on disk - when you want to persist logs for later analysis (this is the running logs file)
        logging.StreamHandler(sys.stdout) # Sends log messages to an output stream usually a standard output or a standard error 
    ]
)

logger = logging.getLogger("mlProjectLogger")