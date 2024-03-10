import time
import requests
import os
import json

class PeerController:
    def garbage_daemon(self):
        while True:
            time.sleep(int(os.getenv("PEERS_GARBAGE_CHECK")))
            self.check_garbage()
    
    def garbage_check(self):
        active_peers = []
        for peer in json.loads(open("database/peers.json").read()):
            ip = peer["ip"]
            retries = int(peer["retries"])
            online = json.loads(requests.get(ip + "/peers/check").text)
            if online == True:
                active_peers.append({"ip": ip, "retries": 0})
            else:
                retries+=1
                if retries >= int(os.getenv["PEERS_GARBAGE_TOLERANCE"]):
                    continue
                active_peers.append({"ip": ip, "retries": int(retries)})
    
    def get_peers(self):
        return json.loads(open("database/peers.json").read())

    def add_peer(self, ip):
        online = json.loads(requests.get("http://" + ip + "/peers/check").text)
        if online == True:
            peers = self.get_peers()
            peers.append({"ip": "http://" + ip, "retries": 0})
            open("database/peers.json", "w").write(json.dumps(peers))