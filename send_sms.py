# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACcc73de3faab23fe2d3761555530b1c37"
auth_token = "a24ad25da26fc114e97ecf69d6302e5c"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+14244027429",
    from_="+18053803506",
    body="I think it's about us having both python2 and 3 and a lot of pips")