#from twilio.rest import Client

 #Your Account SID from twilio.com/console
account_sid = "ACcc73de3faab23fe2d3761555530b1c37"
 # Your Auth Token from twilio.com/console
auth_token  = "a24ad25da26fc114e97ecf69d6302e5c"


from flask import Flask, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
import water


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    #body is the message content sent to us by user
    #number is the phone number of user
    body = request.values.get('Body', None)
    number = request.values.get('From', None)
    #create and update globalbody variabe
    global globalbody 
    #convert to string
    globalbody = str(body)
    #create and update globalnumber
    global globalnumber 
    #convert to string
    globalnumber = str(number)
    
    # print(globalbody)
    # print(globalnumber)
    return redirect(url_for('process'))

@app.route("/process", methods=['GET', 'POST'])
def process():
    #place process here 
    # print(globalbody)
    # print(globalnumber)
    response = water.mymessageCustomer(globalbody)
    #response = globalbody + " " + globalnumber   
    resp = MessagingResponse()
    # Add a message    
    resp.message(response)
    return str(resp)
    
if __name__ == "__main__":
    # app.run(host='127.0.0.1',port=5000)
    app.run(debug=True)