def run_flask(app):
    try:
        app.run(host="0.0.0.0", port=420, debug=True)
    except:
        run_flask()

def run_peers_garbage():
    pass

def run_mempool_garbage():
    pass