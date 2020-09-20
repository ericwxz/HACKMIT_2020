import pandas as pd
import numpy as np
import datetime
import pickle
import location

#use userID and requestID to index the dataframes
#pandas dataframes for storing information about users. 
class All_Users:
	columns = ['username', 'location', 'points', 'contact_info', 'requests', 'fufillments']
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
			self.Users.loc[userID] = user + [[],[]]
			return 1
		
		else: #in database. do nothing
			return 0


	#increment points for a user ID
	def add_point(self, userID):
		"increment points for userID"
		self.Users.loc[userID]['points'] +=1
		return self.Users.loc[userID]['points']


	def save_users(self,filepath):
		"save the users to given filepath as pickle file. filepath ends with a DIRECTOR and / i.e. '/file/path/'"
		filepath = filepath + "users.pkl"
		self.Users.to_pickle(filepath)


	def load_users(self,filepath):
		"loads the users from pickle file at filepath. filepath ends with a DIRECTOR and / i.e. '/file/path/'"
		filepath = filepath + "users.pkl"
		self.Users = pd.read_pickle(filepath)

	





#pandas dataframes for storing infomation about requests
class All_Requests:
	columns = ['requester', 'fufiller', 'time', 'location', 'status', 'description', 'title']
	Requests = pd.DataFrame(columns = columns)

	#list of completed tasks, used for the sucess stories page
	queue = []


	def add_request(self, request, requestID, All_Users):
		"add request data to the Request dataframe. request is a list with the following format:['requester (ID)', 'fufiller (ID)', 'time', 'location', 'status', 'description', 'title'] and requestID is the unique identifier for the request. return 1 on success. All_Users refers to the instance of the All_Users class. status will be set to -1, fufiller will be set to empty string"
		request[1] = "" #making the fufiller null since it has not been fufilled yet
		request[4] = -1 #marking the status as unfufilled
		self.Requests.loc[requestID] = request
		
		#add this requestID to the list of requests made 
		requesterID = request[0]
		All_Users.Users.loc[requesterID]['requests'].append(requestID)

		self.Requests.sort_values(by = ['time'][1], ascending=False, inplace=True)
		return 1

	def add_fufiller(self, requestID, fufillerID, All_Users):
		"add a fufiller to a requestID. the status will be set to 0. All_Users refers to the instance of the All_Users class. return 1 on success"
		self.Requests.loc[requestID]['fufiller'] = fufillerID
		self.Requests.loc[requestID]['status'] = 0
		All_Users.Users.loc[fufillerID]['fufillments'].append(requestID)
		return 1


	def completed_request(self, requestID, All_Users):
		"set reqestID to completed and increment the points for the accessor in the request. Also updates the queue. return 1 on success. All_users refers to the instance of the All_users class, status will be set as 1"
		self.Requests.loc[requestID]['status'] = 1
		All_Users.add_point(self.Requests.loc[requestID]['fufiller'])
		
		
		string = self.Requests.loc[requestID]['description'] +": " + self.Requests.loc[requestID]['location']+ ", " + str(self.Requests.loc[requestID]['time'])
		if len(self.queue) == 5:
			self.queue.pop()
		self.queue = [string] + self.queue
		return 1


	def save_requests(self,filepath):
		"save the users to given filepath as pickle file. filepath ends with a DIRECTOR and / i.e. '/file/path/'"
		filepath = filepath + "requests.pkl"
		self.Requests.to_pickle(filepath)


	def load_requests(self,filepath):
		"loads the users from pickle file at filepath. filepath ends with a DIRECTOR and / i.e. '/file/path/'"
		filepath = filepath + "requests.pkl"
		self.Requests = pd.read_pickle(filepath)
