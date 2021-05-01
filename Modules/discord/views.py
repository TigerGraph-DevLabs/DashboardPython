import sys
sys.path.append("../..")
from DashApp import app


# this package Imports
from flask import  request, render_template

import requests
import json
import pyTigerGraphBeta as tg


configs = {
    "server" : "http://142.93.194.191",
    "user" : "tigergraph",
    "password" : "tigergraphtester",
    "version" : "3.1.0",
    "graph" : "c360",
    "secret" : "94q1hn6bl3lmvkueodthe78e90369n8p",
}

conn = tg.TigerGraphConnection(host=configs["server"], graphname=configs["graph"], username=configs["user"],
                               password=configs["password"], useCert=False)
conn.apiToken = conn.getToken(configs["secret"])

@app.route('/discordUsers')
def discordUsers():
    # users = requests.get("https://community.tigergraph.com/admin/users/list/active.json?order=posts_read", headers=headers)
    # if (users.status_code == 200):
    #     users = users.json()
    #     for user in users:
    #         user['avatar_template'] = user['avatar_template'].replace("{size}", "100")
    users = conn.runInstalledQuery("getMostActiveUsers")[0]["Res"]
    users = [i["attributes"] for i in users]
    for user in range(len(users)):
        users[user]["messages"] = users[user]["@messages"]

    return render_template('discordusers.html', users=users)

