# Download the Python helper library from twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
workspace_sid = "WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
task_sid = "WTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
reservation_sid = "WRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

# redirect using a reservation
reservation = client.taskrouter.workspaces(workspace_sid) \
    .tasks(task_sid).reservations(reservation_sid) \
    .update(instruction='redirect',
            redirect_call_sid='CA123456789',
            redirect_url='http://example.com/assignment_redirect')

print(reservation.reservation_status)
print(reservation.worker_name)