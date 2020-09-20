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
    #return status (capitalized), username, and hash
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
        if status != -1:
            return json.dumps(['result':'Success'])
    return json.dumps({'result':'failure'})

@app.route('/fulfillreq',methods=['POST'])
def fulfillReq():


@app.route('displayreqs',methods=['POST'])
def displayReqs():

@app.route('/userprofile', methods=['POST'])
def fetchProfile():

@app.route('/locationinfo', methods=['POST'])
def locationInfo():
    
