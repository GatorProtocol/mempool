from flask import Flask, Blueprint, Response, request

import json

from controllers.mempoolcontroller import MempoolController

from settings import get_model


mempool_con = MempoolController()
mempool_bp = Blueprint("mempool", __name__)

@mempool_bp.route("/get/<model_id>")
def mempool_get(model_id):
    try:
        return Response(json.dumps(mempool_con.get(model_id), indent=4), mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(json.dumps({"error": e}), mimetype="application/json")

@mempool_bp.route("/add/<model_id>")
def mempool_add(model_id):
    