import os
import sys
import logging

# Define a logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"

log_dir='logs'
log_filepath=os.path.join(log_dir,'logging.log')
os.makedirs(log_dir,exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format=logging_str,   # Set the format for log messages
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output logs to the console
        logging.FileHandler(log_filepath)      # Save logs to a file
    ]
)
logger=logging.getLogger("data science logger")


