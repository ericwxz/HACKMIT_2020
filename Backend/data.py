import pandas as pd
import numpy as np
import datetime

#use userID and requestID to index the dataframes
#pandas dataframes for storing information about users. 
class All_Users:
	columns = ['username', 'location', 'points', 'contact_info']
	Users = pd.DataFrame(columns = columns) #dataframe storing user information

	#hash table of usernames and passwords. use check_user(username, password) to see if user exists and if the user exists, if the correct password was given
	Users_hash = {}

	#check if user exists and checks password
	def check_user(self, username, password):
		"check if a user exists. If user exists, check if password is correct. If user does not exist, return 0. If user exists and password is wrong, return -1. If use exists and password is correct, return 1"
		if username in self.Users_hash:
			if self.Users_hash[username] != password:
				return -1
			return 1
		else:
			return 0

	#functions for adding
	def add_user(self, user, userID, password): #add user. return 1 on sucess, 0 on failure
		"adds user data to User dataframe. User should be a list with the following format: ['username', 'location', 'points', 'contact info']. userID is unique identifier for the user. Return 1 if user is added, return 0 if user was already in database and nothing was done"
		#check if user is already in the databse
		if self.check_user(user[0], password) == 0: #not in database, add to database
			self.Users_hash[user[0]] = password
			self.Users.loc[userID] = user
			return 1
		
		else: #in database. do nothing
			return 0

	#increment points for a user ID
	def add_point(self, userID):
		self.Users.loc[userID]['points'] +=1
		return self.Users.loc[userID]['points']

	





#pandas dataframes for storing infomation about requests
class All_Requests:
	columns = ['requester', 'accesser', 'time', 'location', 'status', 'description']
	Requests = pd.DataFrame(columns = columns)

	#list of completed tasks, used for the sucess stories page
	queue = []


	def add_request(self, request, requestID):
		"add request data to the Request dataframe. request is a list with the following format:['requester (ID)', 'accesser (ID)', 'time', 'location', 'status', 'description'] and requestID is the unique identifier for the request. return 1 on success"
		self.Requests.loc[requestID] = request
		self.Requests.sort_values(by = ['time'], ascending=False, inplace=True)
		return 1


	def completed_request(self, requestID, All_Users):
		"set reqestID to completed and increment the points for the accessor in the request. Also updates the queue. return 1 on success"
		self.Requests.loc[requestID]['status'] = 1
		All_Users.add_point(self.Requests.loc[requestID]['accesser'])
		
		
		string = self.Requests.loc[requestID]['description'] +": " + self.Requests.loc[requestID]['location']+ ", " + str(self.Requests.loc[requestID]['time'])
		if len(self.queue) == 5:
			self.queue.pop()
		self.queue = [string] + self.queue
		return 1
