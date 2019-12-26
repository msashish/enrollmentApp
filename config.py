import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xd5\x06\xcc\xf5\x99I\xd4\x03&\x9d\x8b\x8b\x890\x16\x06'

    MONGODB_SETTINGS = {'db': 'enrollment',
                        'host': 'mongodb://localhost:27017/enrollment'}
