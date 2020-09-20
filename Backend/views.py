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
        contactinfo = request.form.get('locationInfo')
        result = InitializeUser(username, password,contactinfo,locationstate,locationcity,locationzipcode)
        returnval = 'success'
        if result == -1:
            returnval = 'failure'
        return json.dumps({'result':returnval})
