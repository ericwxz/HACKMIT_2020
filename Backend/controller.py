import data
import json
from location import Location

def InitializeUser(username, password, contactInfo, locationstate,locationcity,locationzipcode):
    """Checks if location is initialized; adds to location tree, adds user to database, returns -1 on failure"""
    
    return -1
def LoginUser(username,password):
    """checks if username-password pair exists in db, returns -1 on failure"""
    return -1

#DisplayUserProfile low priority
def DisplayUserProfile(username):
    """returns an array [location, requestIDs, claimIDs, and points]"""
    return -1
def GetUserLoc(username):
    """returns the location of the user"""
    return -1
def InitializeRequest(username, title, description, timeframe, new_location_name = None):
    """initialize data in database with fields listed above, as well as the hidden fields; if new_location not specified, use user default; returns requestID"""
    return -1
def DisplayRequestInfo(requestID):
    """retrieves request info in requesttable: username, location, title, content, timeframe, status, claimant"""

def ClaimRequest(requestID, username):
    """self explanatory, update data fields for request, return the username of the poster for requestID"""

def CompleteRequest(requestID, username):
    """posting user requests to close/complete the request; update points in db"""

def CancelRequest(requestID,username):
    """mark request as completed but do not add points"""

def DisplayLocationInfo(locationname):
    """return location points"""
    node = head.search(locationname)
    if not node:
        print("Unknown location")
        return None
    points = node.points
    return points

def NearbyRequests(locationname):
    """return a list of info-lists on each request under locationname in the form [[requestID1,title1, description1],[requestID2,title2,description2],...]"""

def hashUsername(username):
    return username
def unhashUsername(username):
    return username