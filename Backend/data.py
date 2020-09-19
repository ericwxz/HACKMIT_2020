import pandas as pd
import numpy as np
import datetime

#use userID and requestID to index the dataframes
#pandas dataframes for storing information about users. 
columns = ['username', 'location', 'points']
Users = pd.DataFrame(columns = columns) #dataframe storing user information


#pandas dataframes for storing infomation about requests
columns = ['requester', 'accesser', 'time', 'location', 'status', 'description']
Requests = pd.DataFrame(columns = columns)


#list of completed tasks, used for the sucess stories page
queue = []


#hash table of usernames and passwords. use check_user(username, password) to see if user exists and if the user exists, if the correct password was given
Users_hash = {}


#check if user exists and checks password
def check_user(username, password):
    "check if a user exists. If user exists, check if password is correct. If user does not exist, return 0. If user exists and password is wrong, return -1. If use exists and password is correct, return 1"
    if username in Users_hash:
        if Users_hash[username] != password:
            return -1
        return 1
    else:
        return 0


#functions for adding
def add_user(user, userID, password): #add user. return 1 on sucess, 0 on failure
    "adds user data to User dataframe. User should be a list with the following format: ['username', 'location', 'points']. userID is unique identifier for the user"
    #check if user is already in the databse
    if check_user(user[0], password) == 0: #not in database, add to database
        Users_hash[user[0]] = password
        Users.loc[userID] = user
        return 1
    
    else: #in database. do nothing
        return 0

    

def add_request(request, requestID):
    "add request data to the Request dataframe. request is a list with the following format:['requester (ID)', 'accesser (ID)', 'time', 'location', 'status', 'description'] and requestID is the unique identifier for the request"
    Requests.loc[requestID] = request
    Requests.sort_values(by = ['time'], ascending=False, inplace=True)


def completed_request(requestID):
    "set reqestID to completed"
    Requests.loc['requestID']['status'] = 1
    
    string = Requests.loc['requestID']['description'] +": " + Requests.loc['requestID']['location']+ ", " + str(Requests.loc['requestID']['time'])
    global queue
    if len(queue) == 5:
        queue.pop()
        queue = [string] + queue
