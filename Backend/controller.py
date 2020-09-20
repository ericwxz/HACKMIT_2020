import data
import json

import location
from datetime import datetime

#instantiate classes for storage of user and request data
All_Requests = data.All_Requests()
All_Users = data.All_Users()
head = location.Location()

def InitializeUser(username, password, contactInfo, locationstate,locationcity,locationzipcode):
    "Checks if location is initialized; adds to location tree, adds user to database, returns -1 on failure"
    head.add_entry(locationstate, locationcity, locationzipcode)
    locationcountry = 'USA'
    user = [username, [locationcountry, locationcity, str(locationstate), locationcity], 0, contactInfo]
    userID = hashUsername(username)
    result = All_Users.add_user(user, userID, password)

    if result == 1 or result == 0:
        return 1
    return -1


def LoginUser(username,password):
    "checks if username-password pair exists in db. if user does not exist, return 0. If user exists and password is wrong, return -1. if user exists and password is correct, return 1"
    result = All_Users.check_user(username, password)

    return result


#DisplayUserProfile low priority
def DisplayUserProfile(username):
    "returns an array [location, requestIDs, claimIDs, and points]"
    userID = hashUsername(username)
    location = All_Users.Users.loc[userID]['location']
    requestIDs = All_Users.Users.loc[userID]['requests']
    claimIDs = All_Users.Users.loc[userID]['fufillments']
    points = All_Users.Users.loc[userID]['points']

    return [userID, location, requestIDs, claimIDs, points]


def GetUserLoc(username):
    "returns the location of the user"
    userID = hashUsername(username)
    location = All_Users.Users.loc[userID]['location']

    return location


def InitializeRequest(username, title, content, timeframe, new_location_name = None):
    "initialize data in database with fields listed above, as well as the hidden fields; if new_location not specified, use user default; returns requestID"
    requester_ID = hashUsername(username)
    request = [requester_ID, "", [timeframe, datetime.now()], All_Users.Users.loc[requester_ID]['location'], 0, content, title]
    request_hash = username + content + str(datetime.now())
    request_hash = hash(request_hash)

    result = All_Requests.add_request(request, request_hash, All_Users)
    if result < 1:
        return -1
    return request_hash



def DisplayRequestInfo(requestID):
    "retrieves request info in requesttable: username, location, title, content, timeframe, status, claimant"
    userID = All_Requests.Requests.loc[requestID]['requester']
    username = unhashUsername(userID)
    location = All_Requests.Requests.loc[requestID]['location']
    title = All_Requests.Requests.loc[requestID]['title']
    content = All_Requests.Requests.loc[requestID]['description']
    timeframe = All_Requests.Requests.loc[requestID][0]
    status = All_Requests.Requests.loc[requestID]['status']
    claimantID = All_Requests.Requests.loc[requestID]['fufiller']
    claimant = ""
    if claimantID != "":
        claimant = unhashUsername(claimantID)

    return [username, location, title, content, timeframe, status, claimant]


def ClaimRequest(requestID, username):
    """self explanatory, update data fields for request, return the username of the poster for requestID"""
    userID = hashUsername(username)
    All_Requests.add_fufiller(requestID, userID, All_Users)

    return requestID


def CompleteRequest(requestID, username):
    "posting user requests to close/complete the request; update points in db"
    All_Requests.completed_request(requestID,All_Users)


def CancelRequest(requestID,username):
    "mark request as completed but do not add points"
    All_Requests.Requests.loc[requestID]['status'] = 1


def DisplayLocationInfo(locationname):
    """return location points"""
    node = head.search(locationname)
    if not node:
        print("Unknown location")
        return None
    points = node.points
    return points



def NearbyRequests(locationname):
    "return a list of info-lists on each request under locationname in the form [[requestID1,title1, description1],[requestID2,title2,description2],...]"
    ret_val = []

    for index, row in All_Requests.Requests.iterrows():
        if locationname in row['location']:
            requestID = index
            title = row['title']
            description = row['description']

            arr = [requestID, title, description]
            ret_val.append(arr)

    return ret_val


def hashUsername(username):
    return hash(username)

def unhashUsername(userID):
    username = All_Users.Users.loc[userID]['username']
    return username
