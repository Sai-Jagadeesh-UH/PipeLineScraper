import logging
import os
from datetime import datetime

FILE_NAME = datetime.now().strftime(r"%Y_%m_%d")+".log"

FILE_DIR = os.path.join(os.getcwd(), "logs",
                        datetime.now().strftime("%Y_%m_%d"))

FILE_PATH = os.path.join(FILE_DIR, FILE_NAME)

os.makedirs(FILE_DIR, exist_ok=True)

logging.basicConfig(filename=FILE_PATH,
                    filemode='a', format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')


if __name__ == "__main__":
    logging.info('Logging Successful')
