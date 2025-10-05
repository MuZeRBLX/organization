import os
import json
from functions.version import GetVersion
from functions.updater import Update

HOMEDIR = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HOMEDIR, "data")

if not os.path.isdir(DATA):
    os.makedirs(DATA)  # Creates the directory if it doesn't exist

APPDATA = os.path.join(DATA,"appdata.json")

if not os.path.exists(APPDATA):
    default_data = {
        "VersionNumber": "0.0.0",
        "LastUpdate": "0/0/2000",
        "UpdatesOn": True
    }
    with open(APPDATA, 'w') as f:
        json.dump(default_data, f, indent=4)

apptable = False

with open(APPDATA, 'r') as f:
    apptable = json.load(f)
    
if not apptable["VersionNumber"] == GetVersion() and apptable["UpdatesOn"] == True:
    Update()