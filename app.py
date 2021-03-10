from flask import Flask
from flask import render_template
from flask import request, send_from_directory
import pyTigerGraphBeta as tg 

# configs = {
#     "server" : "https://rasa.i.tgcloud.io",
#     "user" : "tigergraph",
#     "password" : "tigergraph",
#     "version" : "3.1.0",
#     "graph" : "c360",
#     "secret" : "49j0bikopko1kv6lm0a79rk202m7slnk",
# }


app = Flask(__name__, static_url_path='/static')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)

# conn = tg.TigerGraphConnection(host=configs["server"], graphname=configs["graph"], username=configs["user"], password=configs["password"])

# conn.apiToken = conn.getToken(configs["secret"])


# Get Most Starred Repos ?

# GetMostStarred = conn.runInstalledQuery("GetMostStarred")[0]["Result"]
# resSorted = sorted(GetMostStarred, key = lambda i: i['StarCount'],reverse=True)
RepoStarsList = [] # resSorted[:40]

# Get the Most Active Users 

# GetMostActiveUsers = conn.runInstalledQuery("getMostActiveUsers")[0]["Result"]
# usrSorted = sorted(GetMostActiveUsers, key = lambda i: i['valueStars'],reverse=True)
UserStarsList = [] #usrSorted[:20]

# repo Count 
repoCount =  0 #conn.runInstalledQuery("getTotalProjects")[0]["RepoCount"]
repoUsers = 0 #conn.runInstalledQuery("getTotalUsers")[0]["UsersCount"]
repoStars = 0 #conn.runInstalledQuery("GetStarsCount")[0]["StarsCount"]  
repoOwners = 0 #conn.runInstalledQuery("OwnersCount")[0]["OwnersCount"]  

@app.route('/')
def index():
    Github = {
        "repoCount" : repoCount,
        "repoUsers" : repoUsers,
        "repoStars" : repoStars,
        "repoOwners" : repoOwners,
        }
    
    
    return render_template('index.html',Github=Github,RepoStarsList=RepoStarsList,UserStarsList=UserStarsList)



@app.route('/chart')
def testChartAnt():
    import json 
    varList = [
      { 'time': '16 Q1', 'type': 'Test', "value": 0 },
      { 'time': '16 Q1', 'type': 'TEST2', "value": 17.8 },
      { 'time': '16 Q2', 'type': 'TEST2', "value": 69.4 },
      { 'time': '16 Q1', 'type': 'TEST2', "value": 12.8 },
      { 'time': '16 Q3', 'type': 'TEST2', "value": 0 },
      { 'time': '16 Q2', 'type': 'TEST2', "value": 18.1 },

    ]
    print(varList)
    return render_template('chart.html',ListValues=varList)


@app.route('/pie')
def testPieAnt():
   
    return render_template('/G6/LargeGraph.html')

@app.route('/intents')
def intents():
    # try:
    #     res = conn.runInstalledQuery("getUnkownVertex")[0]["ss"]
    # except Exception as e:
    #     print(e)
    res = []
    return render_template('table.html',res=res)


@app.route('/add', methods=['POST'])
def intents_add():
    ids = "Value" #request.form['id']
    return render_template('add.html',ids=ids)



if __name__ == '__main__':
    app.run(debug=True)