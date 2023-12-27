from .settings import *

DEBUG = False

ALLOWED_HOSTS = [
    # 'localhost', '127.0.0.1',
    '10.101.213.121', '10.101.213.122',
    'app.puskeu.polri.info', 'apepe.puskeu.polri.info',
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
