import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "blb bla"
    MONGODB_SETTINGS = {'db':'UTA_Enrollment',
                        "host": "mongodb://192.168.50.4:27017/UTA_Enrollment"}

