# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

credential_list_mapping = client.sip \
    .domains("SD32a3c49700934481addd5ce1659f04d2") \
    .credential_list_mappings \
    .create("CL32a3c49700934481addd5ce1659f04d2")

print(credential_list_mapping.sid)
