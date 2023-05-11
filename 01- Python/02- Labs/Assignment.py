import requests

# Set the access token for your Facebook app
access_token = 'EAATrfHQNlSABAL93Hsk49EidpK0jkCi8AXqmiQFHPJjDZCnxZCQTydFcvhueUxTaQZAArWJri0FX1ReKpmDE6d9i6rOk6KsxdlV3WXXzM36UbSp65rFxCjrBZB1F0ORhFFxxka1ZAZAkrEHn3ZAbDlsf4rlP2gLXi1GudIXMyQhvCAMmfhYEGLDdglYnnWiTx3ExUP3KaSX45nU7meiRFA6'

# Set the content of the message you want to post
message = 'Hello, world!'

# Set the URL for the Graph API endpoint to post a message on your timeline
url = f'https://graph.facebook.com/me/feed?access_token={access_token}'

# Set the data for the POST request
data = {'message': message}

# Send the POST request to the Graph API endpoint
response = requests.post(url, data=data)

# Check the status code of the response to see if the post was successful
if response.status_code == 200:
    print('Post successful')
else:
    print('Post failed')