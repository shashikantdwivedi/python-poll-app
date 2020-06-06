#!/home/ubuntu/miniconda3/envs/poll/bin
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/ubuntu/poll/poll/")

from app import app as application

# TODO - Replace SECRET-KEY with your application secret key
application.secret_key = "SECRET-KEY"
