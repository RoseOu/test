#coding:utf-8

import json
from flask import jsonify,request,Response
from . import api
from .. import db
# from ..models import 

@api.route('/index/', methods=["GET"])
def index():
    return jsonify({
        "index":"hihihihihi"
    })