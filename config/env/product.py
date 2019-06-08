# -*- coding: UTF-8 -*-
DEBUG = False

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PWD = 'promethues'
REDIS_DB_ZERO = 0
REDIS_DB_ONE = 1
REDIS_SSL = False
REDIS_URL = 'redis://:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'.format(REDIS_HOST=REDIS_HOST,
                                                                               REDIS_PORT=REDIS_PORT,
                                                                               REDIS_PWD=REDIS_PWD,
                                                                               REDIS_DB=REDIS_DB_ONE)

CACHES_REDIS_URL = 'redis://:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'.format(REDIS_HOST=REDIS_HOST,
                                                                               REDIS_PORT=REDIS_PORT,
                                                                               REDIS_PWD=REDIS_PWD,
                                                                               REDIS_DB=REDIS_DB_ONE)

MYSQL_DB_ENGINE = 'django.db.backends.mysql'
MYSQL_DB_NAME = 'prod'
MYSQL_DB_USER = 'prod'
MYSQL_DB_PASSWORD = '123456'
MYSQL_DB_HOST = '127.0.0.1'
MYSQL_DB_PORT = '3306'
