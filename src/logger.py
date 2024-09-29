import logging
import os #provide functionality for the reading and writing events
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y"_%H_%M_%s')}.log"

#now make path , logs_path me getcwd(give path of current working directory) logs and log_file ko join karega
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# pwd() and os.getpwd() both work same
# pwd() / logs / LOG_FILE ye sab lo join karega
# exist_ok if directory already present then dont throw error
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] % (lineno)d % (name)s - %(levelname)s -  %(message)s",
    level = logging.INFO
)