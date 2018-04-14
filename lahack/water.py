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
                docs_ref = users_ref.document(doc.id)
                deleteend = "messageList." + msg + ".endTime" 
                deletestart = "messageList." + msg + ".startTime" 
                deletebody = "messageList." + msg + ".body" 
                docs_ref.update({
                deleteend: u'',
                deletestart: u'',
                deletebody: u''})
        i += 1


# users_ref = db.collection(u'restaurant')
# docs = users_ref.get()

# doc_ref = db.collection(u'restaurant').document(phoneNumber)
# doc_ref.update({
# 	u'messageList.message1.body': u'',
# 	u'messageList.message1.startTime': u'',
# 	u'messageList.message1.endTime': u''})



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

# doc_ref = db.collection(u'restaurant').document(u'+14244027429')
# doc_ref.set({
#     u'phone': u'+14244027429',
#     u'name': u'Subway',
#     u'zipCode': u'90024',
#     u'address': u'940 Westwood Plaza',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message2': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message3': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#     },
# })

# doc_ref = db.collection(u'restaurant').document(u'+14245356908')
# doc_ref.set({
#     u'phone': u'+14245356908',
#     u'name': u'Subway',
#     u'zipCode': u'90025',
#     u'address': u'777 Irvine',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message2': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message3': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#     },
# })

# doc_ref = db.collection(u'grocery').document(u'+14245356908')
# doc_ref.set({
#     u'phone': u'+14244027429',
#     u'name': u'Pressure Cooker Seller',
#     u'zipCode': u'90024',
#     u'address': u'1400 Westwood Blv',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message2': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message3': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#     },
# })

# doc_ref = db.collection(u'grocery').document(u'+13108492468')
# doc_ref.set({
#     u'phone': u'+13108492468',
#     u'name': u'7/11',
#     u'zipCode': u'90024',
#     u'address': u'1300 Westwood Blv',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message2': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message3': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#     },
# })

# doc_ref = db.collection(u'grocery').document(u'+13109233881')
# doc_ref.set({
#     u'phone': u'+13109233881',
#     u'name': u'Trader Joes',
#     u'zipCode': u'90024',
#     u'address': u'1000 Glendon Avenue',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message2': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#         u'message3': {
#             u'body': u'',
#             u'numberOfItems': u'',
#         },
#     },
# })
# doc_ref = db.collection(u'restaurant').document(u'+13108492468')
# doc_ref.set({
#     u'phone': u'+13108492468',
#     u'name': u'Coffee Bean',
#     u'zipCode': u'90024',
#     u'address': u'125 Westwood Avenue',
#     u'messageList': {
#         u'message1': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message2': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#         u'message3': {
#             u'body': u'',
#             u'startTime': u'',
#             u'endTime': u''
#         },
#     },
# })


def mymessageCustomer(zipCode):         #zipcode is of this format: zip space rest/groc
    delete_all_old()
    mylist=[]
    newlist = zipCode.split()
    if(len(newlist) != 2):
        return ("Error: wrong format")
    print(newlist[1])
    if (newlist[1] == "restaurant"):
        users_ref = db.collection(u'restaurant')
    if (newlist[1] == "grocery"):
        users_ref = db.collection(u'grocery')
    docs = users_ref.get()
    for doc in docs :
        if(doc.to_dict()[u'zipCode'] == newlist[0]):
            mylist.append(doc)
    if (len(mylist) < 2):
        print("Error: input")
    i = 1
    finalmsg = ""
    for doc in mylist:
        printMsg = str(i) + ". " + doc.to_dict()[u'name'] + " at " + doc.to_dict()[u'address'] 
        mert = 0
        for msg in doc.to_dict()[u'messageList']:
            if (newlist[1] == "restaurant"):
                if(doc.to_dict()[u'messageList'][msg][u'body'] != ''):
                    first = str(doc.to_dict()[u'messageList'][msg][u'body'], 'utf-8')
                    second = str(doc.to_dict()[u'messageList'][msg][u'endTime'], 'utf-8')
                    third = str(doc.to_dict()[u'messageList'][msg][u'startTime'], 'utf-8')
                    printMsg += '\n' + first + " starting at " + third + " ending at " + second
                    mert = 1
            elif (newlist[1] == "grocery"):
                if(doc.to_dict()[u'messageList'][msg][u'body'] != ''):
                    first = str(doc.to_dict()[u'messageList'][msg][u'body'], 'utf-8')
                    printMsg += '\n' + first + " available until supplies last"
                    mert = 1
        if mert == 0:
            printMsg = ""
        else:
            i += 1
            finalmsg += printMsg + '\n' + '\n'
    if finalmsg == "":
        return "No current offers!"
    return finalmsg


# def main():					# should be getting user response for server name
# 	if(len(sys.argv) != 2):
# 		print("Error!")
# 	zipCode = sys.argv[1]		# sets message to what we input
# 	try:
# 	    returntype = mymessageCustomer(zipCode)
# 	except KeyboardInterrupt:
# 	    pass
# 	# Close the server

# if __name__ == "__main__":
#     main()
