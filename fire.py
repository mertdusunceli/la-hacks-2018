import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import string
import datetime

# Use a service account
cred = credentials.Certificate('/Users/mertdusunceli/Desktop/serviceaccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def delete_all_old():
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	stringtime = str(hour) + str(minute)
	# doc_ref = db.collection(u'restaurant').document(phoneNumber)
	i = 1
	users_ref = db.collection(u'restaurant')
	docs = users_ref.get()
	for doc in docs:
		# printMsg = str(i) + " " + doc.to_dict()[u'name'] + " at " + doc.to_dict()[u'address'] 
		for msg in doc.to_dict()[u'messageList']:
			if(doc.to_dict()[u'messageList'][msg][u'endTime'] != '' and int(doc.to_dict()[u'messageList'][msg][u'endTime']) < int(stringtime)):
				#delete
				print(doc.id)
				docs_ref = users_ref.document(doc.id)
				deleteend = "messageList." + msg + ".endTime" 
				deletestart = "messageList." + msg + ".startTime" 
				deletebody = "messageList." + msg + ".body" 
				docs_ref.update({
				deleteend: u'',
				deletestart: u'',
				deletebody: u''})
		i += 1





	# users_ref = db.collection(u'users')
	# docs = users_ref.get()

	# for doc in docs:
	#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

	# db.collection(u'restaurant').document(u'phoneNumber').delete()

	# doc_ref = db.collection(u'restaurant').document(u'9119119111')
	# doc_ref.set({
	#     u'phone': u'9119119111',
	#     u'name': u'Chick Fil a',
	#     u'zipCode': u'90024',
	#     u'address': u'450 Westwood Plaza',
	#     u'messageList': {
	#     	u'message1': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message2': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message3': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     },
	# })

	# doc_ref = db.collection(u'restaurant').document(u'1231231234')
	# doc_ref.set({
	#     u'phone': u'1231231234',
	#     u'name': u'Subway',
	#     u'zipCode': u'90024',
	#     u'address': u'940 Westwood Plaza',
	#     u'messageList': {
	#     	u'message1': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message2': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message3': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     },
	# })

	# doc_ref = db.collection(u'restaurant').document(u'9876432111')
	# doc_ref.set({
	#     u'phone': u'9876432111',
	#     u'name': u'Subway',
	#     u'zipCode': u'90025',
	#     u'address': u'777 Irvine',
	#     u'messageList': {
	#     	u'message1': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message2': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     	u'message3': {
	#     		u'body': u'Empty',
	#     		u'startTime': 10,
	#     		u'endTime': 12
	#     	},
	#     },
	# })

# users_ref = db.collection(u'restaurant')
# docs = users_ref.get()

def mymessage(call, phoneNumber):
	# find the rest in database .get(rest)
	delete_all_old()
	newcall = call.split()
	if (len(newcall) == 2 and (newcall[1] == "G1" or newcall[1] == "G2" or newcall[1] == "G3") and newcall[0] == "STOP"):
		doc_ref = db.collection(u'grocery').document(phoneNumber)
		code = newcall[1]
		printer = "STOP message recorded for " + code + ": "
		if(code == "G1"):
			printer += docs.to_dict()[u'messageList'][u'message1'][u'body']
			doc_ref.update({
				u'messageList.message1.body': u''})
		elif(code == "G2"):
			printer += docs.to_dict()[u'messageList'][u'message2'][u'body']
			doc_ref.update({
				u'messageList.message2.body': u'',})		
		elif(code == "G3"):
			printer += docs.to_dict()[u'messageList'][u'message3'][u'body']
			doc_ref.update({
				u'messageList.message3.body': u'',})
		else:
			return("Error 4 : no message at that location")
		return printer

	elif (newcall[0] == "G1" or newcall[0] == "G2" or newcall[0] == "G3"):
		doc_ref = db.collection(u'grocery').document(phoneNumber)
		code = newcall[0]
		messagequote = call.split('\"')
		if(code == "G1"):
			doc_ref.update({
				u'messageList.message1.body': messagequote[1],})
		elif(code == "G2"):
			doc_ref.update({
				u'messageList.message2.body': messagequote[1],})
		elif(code == "G3"):
			doc_ref.update({
				u'messageList.message3.body': messagequote[1],})
		else:
			return("Error 4 : no message at that location")
		doc_ref = db.collection(u'grocery').document(phoneNumber)
		docs = doc_ref.get()
		i = 1
		printMsg = "Your current offers are:" + '\n'
		for msg in docs.to_dict()[u'messageList']:
			if(docs.to_dict()[u'messageList'][msg][u'body'] != ''):
				printMsg += str(i) + ". " + docs.to_dict()[u'messageList'][msg][u'body'] + " available until supplies last" '\n'
				i += 1
		return printMsg


	elif(len(newcall) == 2 or len(newcall) > 3):		# it is either 2 or greater than 3
		doc_ref = db.collection(u'restaurant').document(phoneNumber)
		if (len(newcall) == 2):
			#remove from database
			printer = "STOP message recorded for " + str(int(newcall[1])) + ": "
			if (newcall[0] != "STOP"):
				return "STOP is invalid"
			code = int(newcall[1])
			if(newcall[1] == '1'):
				printer += docs.to_dict()[u'messageList'][u'message1'][u'body']
				doc_ref.update({
					u'messageList.message1.body': u'',
					u'messageList.message1.startTime': u'',
					u'messageList.message1.endTime': u''})
			elif(newcall[1] == '2'):
				printer += docs.to_dict()[u'messageList'][u'message2'][u'body']
				doc_ref.update({
					u'messageList.message2.body': u'',
					u'messageList.message2.startTime': u'',
					u'messageList.message2.endTime': u''})
			elif(newcall[1] == '3'):
				printer += docs.to_dict()[u'messageList'][u'message3'][u'body']
				doc_ref.update({
					u'messageList.message3.body': u'',
					u'messageList.message3.startTime': u'',
					u'messageList.message3.endTime': u''})
			else:
				return("Error 4 : no message at that location")
			return printer			#delete from database
		else:															#here message is greater/equal to 4
			iter = len(newcall)
			messagequote0 = call.split('\"')
			if(len(messagequote0) != 3):
				return ("Error 3")
			if(newcall[0] == '1'):
				doc_ref.update({
					u'messageList.message1.body': messagequote0[1],
					u'messageList.message1.startTime': (newcall[iter - 2]),
					u'messageList.message1.endTime': newcall[iter - 1]})
			elif(newcall[0] == '2'):
				doc_ref.update({
					u'messageList.message2.body': messagequote0[1],
					u'messageList.message2.startTime': newcall[iter - 2],
					u'messageList.message2.endTime': newcall[iter - 1]})
			elif(newcall[0] == '3'):
				doc_ref.update({
					u'messageList.message3.body': messagequote0[1],
					u'messageList.message3.startTime': newcall[iter - 2],
					u'messageList.message3.endTime': newcall[iter - 1]})
			else:
				return("Error 4 : no message at that location")
		doc_ref = db.collection(u'restaurant').document(phoneNumber)
		docs = doc_ref.get()
		i = 1
		printMsg = "Your current offers are:" + '\n'
		for msg in docs.to_dict()[u'messageList']:
			if(docs.to_dict()[u'messageList'][msg][u'body'] != ''):
				printMsg += str(i) + ". " + docs.to_dict()[u'messageList'][msg][u'body'] + " starting at " +  docs.to_dict()[u'messageList'][msg][u'startTime'] + " ending at " + docs.to_dict()[u'messageList'][msg][u'endTime'] + '\n'
				i += 1
		return printMsg
	else: 
		wrong = "Wrong input"
		return wrong


# ourlist = [newcall[0], messagequote0[1],newcall[iter - 2], newcall[iter - 1]]		# print 
# savingmsg = cal
# return  (ourlist[0] + ' ' + ourlist[1] + ' ' + ourlist[2] + ' ' + ourlist[3])

"""
def main():					# should be getting user response for server name
if(len(sys.argv) != 3):
	print("Error!")
message = sys.argv[1]		# sets message to what we input
phoneNumber = sys.argv[2]	# rest code 
try:
    returntype = mymessage(message, phoneNumber)
except KeyboardInterrupt:
    pass
# Close the server
print(returntype)

if __name__ == "__main__":
main()

"""








