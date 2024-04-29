from twilio.rest import Client

account_sid = "abcde"
auth_token = "kjwbfuwfho1uebkbv"

client = Client(account_sid, auth_token)
client.messages.create(
    to="...",
    from_="...",
    body="This is a test message"
)
