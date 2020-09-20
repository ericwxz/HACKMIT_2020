from Backend import app
from flask import render_template, request, redirect
from controller import *
import json

@app.route('/signup',methods=['POST'])
def create_user():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('password')
        passwordcheck = request.form.get('passwordcheck')
        locationstate = request.form.get('locationstate')
        locationcity = request.form.get('locationcity')
        locationzipcode = request.form.get('locationzipcode')
        contactinfo = request.form.get('contactinfo')
        result = InitializeUser(username, password,contactinfo,locationstate,locationcity,locationzipcode)
        returnval = 'Success'
        if result == -1:
            returnval = 'Failure'
        return json.dumps({'result':returnval, 'userKey':username,'hash':hashUsername(username)})
    else:
        return json.dumps({'result':'failure'})

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        result = LoginUser(username,password)
        returnval = 'Success'
        if result == -1:
            returnval = 'Failure'
        return json.dumps({'result':returnval, 'userKey':username,'hash':hashUsername(username)})
    else:
        return json.dumps({'result':'failure'})

@app.route('/newreq',methods=['POST'])
def newReq():
    if request.method=='POST':
        username = request.form.get('userkey')
        title = request.form.get('title')
        description = request.form.get('description')
        timeframe = request.form.get('timeframe')
        category = request.form.get('category')
        location = GetUserLoc(username)
        requestID = InitializeRequest(username, title, description, timeframe, location)
        if requestID != -1:
            return json.dumps({'result':'Success', 'requestID':requestID})
    else:
        return json.dumps({'result':'failure'})


@app.route('/cancelreq',methods=['POST'])
def cancelReq():
    if request.method=='POST':
        username = request.form.get('userkey')
        requestID = request.form.get('requestID')
        CancelRequest(requestID,username)
    return json.dumps(['result':'Who cares?'])

@app.route('/claimreq', methods=['POST'])
def claimReq():
    if request.method=='POST':
        claimer = request.form.get('userkey')
        requestID = request.form.get('requestID')
        status = ClaimRequest(requestID,claimer)
        return json.dumps(['result':'Success'])
    return json.dumps({'result':'Failure'})

@app.route('/fulfillreq',methods=['POST'])
def fulfillReq():
    if request.method=='POST':
        requestID = request.form.get('requestID')
        username = request.form.get('username')
        CompleteRequest(requestID,username)
        return json.dumps(['result':'Success'])
    return json.dumps({'result':'Failure'})

@app.route('displayreqs',methods=['POST'])
def displayReqs():
    if request.method=='POST':
        location = request.form.get('location')
        reqlist = NearbyRequests(location)
        return json.dumps({'reqID'+str(i):reqlist[i][0], 'title'+str(i):reqlist[i][1], 'description'+str(i):reqlist[i][2]})

@app.route('/userprofile', methods=['POST'])
def fetchProfile():
    if request.method=='POST':
        username = request.form.get('username')
        arr = DisplayUserProfile(username)
        return json.dumps({'location':arr[0],'requestIDs':arr[1],'claimIDs':arr[2],'points':arr[3]})

@app.route('/locationinfo', methods=['POST'])
def locationInfo():
    if request.method=='POST':
        name = request.form.get('name')
        points = DisplayLocationInfo(name)
        return json.dumps({'points':points})

@app.route('/requestinfo',methods=['POST'])
def viewRequestInfo():
    if request.method=='POST':
        requestID = request.form.get('requestID')
        arr = DisplayRequestInfo(requestID)
        return json.dumps({'username':arr[0],'location':arr[1],'title':arr[2],'description':arr[3],'timeframe':arr[4],'status':arr[5],'claimant':arr[6]})