import sys
sys.path.append("../..")
from DashApp import app



# this package Imports
from flask import  request, render_template
import requests
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

# Get Most Starred Repos ?

GetMostStarred = conn.runInstalledQuery("GetMostStarred")[0]["Result"]
resSorted = sorted(GetMostStarred, key=lambda i: i['StarCount'], reverse=True)
RepoStarsList = resSorted[:40]

# Get the Most Active Users

GetMostActiveUsers = conn.runInstalledQuery("getMostActiveUsers")[0]["Result"]
usrSorted = sorted(GetMostActiveUsers, key=lambda i: i['valueStars'], reverse=True)
UserStarsList = usrSorted[:20]

# repo Count
repoCount = conn.runInstalledQuery("getTotalProjects")[0]["RepoCount"]
repoUsers = conn.runInstalledQuery("getTotalUsers")[0]["UsersCount"]
repoStars = conn.runInstalledQuery("GetStarsCount")[0]["StarsCount"]
repoOwners = conn.runInstalledQuery("OwnersCount")[0]["OwnersCount"]


@app.route('/')
def index():
    Github = {
        "repoCount": repoCount,
        "repoUsers": repoUsers,
        "repoStars": repoStars,
        "repoOwners": repoOwners,
    }

    return render_template('index.html', Github=Github, RepoStarsList=RepoStarsList, UserStarsList=UserStarsList)


@app.route('/chart')
def testChartAnt():
    varList = [
        {'time': '16 Q1', 'type': 'Test', "value": 0},
        {'time': '16 Q1', 'type': 'TEST2', "value": 17.8},
        {'time': '16 Q2', 'type': 'TEST2', "value": 69.4},
        {'time': '16 Q1', 'type': 'TEST2', "value": 12.8},
        {'time': '16 Q3', 'type': 'TEST2', "value": 0},
        {'time': '16 Q2', 'type': 'TEST2', "value": 18.1},

    ]
    print(varList)
    return render_template('chart.html', ListValues=varList)


@app.route('/schema')
def showSchema():
    return render_template('schema.html')


@app.route('/pie')
def testPieAnt():
    return render_template('/G2/CalendarHeatmap.html')


@app.route('/intents')
def intents():
    # try:
    #     res = conn.runInstalledQuery("getUnkownVertex")[0]["ss"]
    # except Exception as e:
    #     print(e)
    res = []
    return render_template('table.html', res=res)


@app.route('/add', methods=['POST'])
def intents_add():
    ids = "Value"  # request.form['id']
    return render_template('add.html', ids=ids)