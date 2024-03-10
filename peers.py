from flask import Flask, Blueprint, Response, request

import json

from controllers.peercontroller import PeerController

peer_con = PeerController()

peers_bp = Blueprint("peers", __name__, url_prefix="/peers")

@peers_bp.route("/check")
def peers_check():
    return Response(json.dumps({"online": True}), mimetype="application/json")

@peers_bp.route("/connect")
def peer_connect():
    ip = request.remote_addr
    peer_con.add_peer(ip)
    return Response(json.dumps({"connected": True}), mimetype="application/json")

@peers_bp.route("/list")
def peer_list():
    return peer_con.get_peers()