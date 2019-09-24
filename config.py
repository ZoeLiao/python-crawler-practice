from redis import StrictRedis

MONGO_USER = 'root'
MONGO_URL_PTT = "mongodb://localhost:27017/ptt"
MONGO_URL_NEWS = "mongodb://localhost:27017/news"

rs_host = 'localhost'
rs_port = 6379
rs_db = 0
rs_password = None
rs = StrictRedis(host=rs_host, port=rs_port, db=rs_db, password=rs_password, socket_connect_timeout=5)


try:
    from local_config import *
except ImportError:
    pass
