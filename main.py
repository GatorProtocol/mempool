import threading

from flask import Flask

from mempool import mempool_bp
from peers import peers_bp

from runtime import run_flask, run_peers_garbage, run_mempool_garbage

app = Flask(__name__)
app.register_blueprint(mempool_bp)
app.register_blueprint(peers_bp)

flask_thread = threading.Thread(target=run_flask)
peers_garbage_thread = threading.Thread(target=run_peers_garbage)
mempool_garbage_thread = threading.Thread(target=run_mempool_garbage)