import sys
sys.path.append("../..")
from DashApp import app


# this package Imports
from flask import  request, render_template
import requests


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'Api-Key' : '360ff2183c95508261fe9c72469821368d91ddd6f324e5197790a64feab6a1b4',
    'Api-Username': 'Zrouga'
}


@app.route('/communityOverview')
def communityOverview():
    stats = requests.get("https://community.tigergraph.com/about.json", headers=headers)
    if (stats.status_code == 200):
        stats = stats.json()['about']['stats']
    return render_template('communityOverview.html', stats=stats)


@app.route('/communityUsers')
def communityUsers():
    users = requests.get("https://community.tigergraph.com/admin/users/list/active.json?order=posts_read",
                         headers=headers)
    if (users.status_code == 200):
        users = users.json()
        for user in users:
            user['avatar_template'] = user['avatar_template'].replace("{size}", "100")
    return render_template('communityUsers.html', users=users)


@app.route('/discourse/fetch/', methods=['POST', 'GET'])
def fetchData():
    pageviews = []
    signups = []
    posts = []
    topics = []
    likes = []
    if request.method == 'POST':
        dates = request.json['data']
        url = f"https://community.tigergraph.com/admin/reports/consolidated_page_views.json?{dates}"
        res = requests.get(url, headers=headers)
        if (res.status_code == 200):
            pageviews = res.json()['report']['data']

        url = f"https://community.tigergraph.com/admin/reports/signups.json?{dates}"
        res = requests.get(url, headers=headers)
        if (res.status_code == 200):
            signups = res.json()['report']['data']

        url = f"https://community.tigergraph.com/admin/reports/posts.json?{dates}"
        res = requests.get(url, headers=headers)
        if (res.status_code == 200):
            posts = res.json()['report']['data']

        url = f"https://community.tigergraph.com/admin/reports/topics.json?{dates}"
        res = requests.get(url, headers=headers)
        if (res.status_code == 200):
            topics = res.json()['report']['data']

        url = f"https://community.tigergraph.com/admin/reports/likes.json?{dates}"
        res = requests.get(url, headers=headers)
        if (res.status_code == 200):
            likes = res.json()['report']['data']

    return {"pageviews": pageviews, "signups": signups, "posts": posts, "topics": topics, "likes": likes}
