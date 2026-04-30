# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# LOG_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# if __name__ == "__main__":
#     logging.info("Logging has started.")
import logging
import os
from datetime import datetime

# 1. Create the filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create the directory path (just the 'logs' folder)
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# 3. Join the directory path and the filename into one final path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s",
    level=logging.INFO
)

