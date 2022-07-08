"""Python TCP Socket Web Server"""

import logging
import socket
import sys
import time


##############################################################################

# Define port server listens on
HOST_ADDRESS = '0.0.0.0'
PORT_NUMBER = 8080

##############################################################################

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="[Dummy-Server] [%(asctime)s] [%(levelname)-7s] : %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger()


class HealthCheckServer:
    """Dummy TCP socket server to allow for TCP health checks"""

    def __init__(self, ip:str = HOST_ADDRESS, port:int = PORT_NUMBER, retry_count:int = 5):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.retry_count = retry_count
        self.current_try_count = 0

    def accept_and_close(self) -> None:
        """Wait for client connection. Once connected, close connection"""
        while True:
            logger.info(f'Waiting for client connection ...')
            try:
                connection, client_address = self.sock.accept()
            except KeyboardInterrupt:
                logger.warning(f"User pressed CTRL-C. Exiting server ...")
                sys.exit(0)

            logger.info(f"Client connected. Client IP {client_address[0]}, port {client_address[1]}")
            connection.close()
            logger.info(f"Client connection closed\n")

    def start(self) -> None:
        """Starting web server"""
        logger.info(f"Starting dummy server on {self.ip}, port {self.port} ...")
        server_address = (self.ip, self.port)

        if self.current_try_count > self.retry_count:
            logger.info(f"Failed to start dummy server")
            return

        try:
            self.current_try_count += 1
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind(server_address)
            self.sock.listen(1)
            self.accept_and_close()
        except socket.error:
            logger.error(f"Failed to start dummy server. Retrying in 5 seconds ...")
            time.sleep(5)
            self.start()
        except Exception as error:
            logger.error(f"Failed to start dummy server. Exception: {error}")


if __name__ == '__main__':
    """Main program entrypoint"""
    server = HealthCheckServer()
    server.start()

