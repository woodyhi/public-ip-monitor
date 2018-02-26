import logging
import os

import time

import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/log/'
if not os.path.exists(dir):
    os.makedirs(dir)

filepath = dir +  time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + '.txt'

# create a file handler
handler = logging.FileHandler(filepath, encoding='utf-8')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def log(msg):
    logger.info(msg)