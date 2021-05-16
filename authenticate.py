import requests
import json

url = "https://api.symbl.ai/oauth2/token:generate"

appId = "527a5770576c446a794e306e6357544c79756b3854424d53675659644e59746c"  # App Id found in your platform
appSecret = "5935695f794b3569736662503651365a446351366f4163566e505935636f74497a447534323477623777586d446d556650533469365a746f66624f4648336f58"  # App Id found in your platform

payload = {
    "type": "application",
    "appId": appId,
    "appSecret": appSecret
}
headers = {
    'Content-Type': 'application/json'
}

responses = {
    400: 'Bad Request! Please refer docs for correct input fields.',
    401: 'Unauthorized. Please generate a new access token.',
    404: 'The conversation and/or it\'s metadata you asked could not be found, please check the input provided',
    429: 'Maximum number of concurrent jobs reached. Please wait for some requests to complete.',
    500: 'Something went wrong! Please contact support@symbl.ai'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    # Successful API execution
    print("accessToken => " + response.json()['accessToken'])  # accessToken of the user
    print("expiresIn => " + str(response.json()['expiresIn']))  # Expiry time in accessToken
elif response.status_code in responses.keys():
    print(responses[response.status_code], response.text)  # Expected error occurred
else:
    print("Unexpected error occurred. Please contact support@symbl.ai" + ", Debug Message => " + str(response.text))

exit()

#returned access token eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjYwODk2Njk5MzY2NzY4NjQiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiUnpXcFdsRGp5TjBuY1dUTHl1azhUQk1TZ1ZZZE5ZdGxAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjIxMTQ4ODg4LCJleHAiOjE2MjEyMzUyODgsImF6cCI6IlJ6V3BXbERqeU4wbmNXVEx5dWs4VEJNU2dWWWROWXRsIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.NYvMHt5CyfqOg8gwe5VatnfRkyfYCD7-8FDjLC7dz93ZikQkcvsW4iPGzpHM5EZ85r0OFOTwMMLK5T8KhR1CSKfUBDHRGYe7m3SeslzOtKc0PI_LVzsLrhAbmiZJI1f7hd4z7LTixhoMZ4SD8GeG9I64czYTRUy1aL9H1gJdyq31V7NxDDX4JpOm3mcGVMZYlAz_lRHB0m7xOMTPwCDsy1g8mbI5m8BWxQ8s3aYIQJizVLfvchWffzfU9vlpoMaka9Kd403dOGifTPpou1S1lRQ0jOha0YeYEs_GqTPn_lfpbb-A4sdLXdv5Y6VslLEqrKGk1jfHd5mGZGrdBNTKCg
