import logging
from datetime import datetime
import os

# Directory to store log files
LOG_DIR = "housing_logs"

# Current Timestamp in the format "YYYY-MM-DD_HH-MM-SS"
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Log file name with the current timestamp
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# Ensure that the log directory exists, creating it if necessary
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log file path
    filemode="w",  # Write mode, creates a new file if it doesn't exist
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Logging level (INFO and above)
)

# At this point, logging is configured, and you can use the logger throughout your code.

# Example usage:
# logger = logging.getLogger(__name__)
# logger.info("This is an informational message.")
# logger.warning("This is a warning.")
# logger.error("An error occurred.")

def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]
