import logging
import os
import sys
import time

logging.basicConfig(level=logging.INFO)
loggerer = logging.getLogger(__name__)

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
loggerer.addHandler(handler)


def log(msg):
    loggerer.info(msg)