"""Python HTTP/HTTPS web server"""

import logging
import os

from flask import Flask


##############################################################################

# Define commands to check for if status is healthy
COMMAND1 = "date"
COMMAND2 = "hostname"

##############################################################################

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="[Dummy-Server] [%(asctime)s [%(levelname)-7s] : %(message)s]",
    datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger()

application = Flask(__name__)

@application.route('/health', methods=["GET"])
def health():
    """Health Check endpoint"""
    logger.info("Checking health (/health) ...")

    success_command_1 = not bool(os.system(COMMAND1 + "> /dev/null"))
    logger.info(f'    - Command 1 success: {success_command_1}')

    success_command_2 = not bool(os.system(COMMAND2 + "> /dev/null"))
    logger.info(f'    - Command 2 success: {success_command_2}')

    healthy = all([success_command_1, success_command_2])
    logger.info(f'    - Health status:     {healthy}')

    status_code = 200 if healthy else 500
    return {"success_command_1": success_command_1, "success_command_2": success_command_2, "healthy": healthy}, status_code

