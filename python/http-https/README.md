# Python HTTP/HTTPS Web Server

:exclamation: **WARNING** These web servers are for development, testing, and troubleshooting only 

## Dependencies

- Python 3.7 or above
- `pip install flask`
- `pip install gunicorn` (More official)

## Usage

### HTTP Server

- Flask: `FLASK_APP=dummy_server flask run --host 0.0.0.0 --port 8080`
- Gunicorn: `gunicorn dummy_server --bind 0.0.0.0:8080`


### HTTPS Server

**Temporary Self-Signing Certificate**

1. Install pyOpenSSL 
    - `pip install pyopenssl`
2. Run server
    - `FLASK_APP=dummy_server flask run --cert=adhoc`

**Using Your Own Certificate**

1. Install `openssl`
2. Generate Certificate
    - `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`
2. Run server
    - Flask: `FLASK_APP=dummy_server flask run --host 0.0.0.0 --port 8080 --cert=cert.pem --key=key.pem`
    - Gunicorn: `gunicorn dummy_server --bind 0.0.0.0:8080 --certfile cert.pem --keyfile key.pem`

