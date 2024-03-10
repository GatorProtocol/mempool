import subprocess
import importlib
import sys

import json

######  Dependency Checks
## Global
try:
    subprocess.check_call([f"{sys.executable}", "-r", "pip", "install", "requirements.txt"])
except:
    raise Exception("Unable to install global dependencies")

## Models
deps = json.loads(open("database/settings.json").read())
for dep in deps:
    try:
        importlib.import_module(dep)
    except:
        subprocess.check_call([f"{sys.executable}", "-m", "pip", "install", str(dep)])

