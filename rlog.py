from datetime import datetime
from functools import wraps
from flask import request
from confs.config import PROJECT_NAME as app_name

log_db = None
try:
    from uitls.mongo import mongodb
    log_db = mongodb.liang_cloud_api.logs
except Exception as e:
    from confs.config import MONGO_URI
    from pymongo import MongoClient
    mongodb = MongoClient(MONGO_URI, connect=False)
    log_db = mongodb.liang_cloud_api.logs


def print_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        uid = request.user.get("u_id")
        cid = request.user.get("c_id")
        username = request.user.get("name") \
                   or request.cookies.get("username")
        phone = request.user.get("phone") \
                or request.cookies.get("phone")
        account = request.user.get("email") \
                  or request.user.get("account") \
                  or request.cookies.get("email") \
                  or request.cookies.get("account") \
                  or phone
        data = request.json or request.args
        op = func.__name__
        res = func(*args, **kwargs)
        op_info = op+(" Success!" if res.json.get("code") == 0 else " Failed!")
        log_info = {
            "uid": uid,
            "cid": cid,
            "username": username,
            "phone": phone,
            "account": account,
            "app": app_name,
            "op": op_info,
            "data": data,
            "time": datetime.now()
        }
        log_db.insert(log_info)
        print(log_info)
        return res
    return wrapper
