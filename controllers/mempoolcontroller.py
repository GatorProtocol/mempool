import time
import os
import requests
import json

from settings import get_model, get_models

from algorithms import mempool_sorting_algorithm

import threading

class MempoolController:
    def __init__(self):
        self.txstructure = {
            "entropy": "",
            "prompt": "",
            "id": "",
            ""
        }
    
    def all(self):
        return json.loads(open("database/mempool/active.json").read())

    def get(self, model_id):
        all = self.all()
        new = []
        for item in all:
            if int(item["id"]) == int(model_id):
                new.append(all)
        return new

    def add(self, ipfrom=None, prompt=None, tx=, entropy=None, modelid=None, price=None, confirmations=None):
        open("database/mempool/")
    
    def updatestate():
        if 