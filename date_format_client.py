from requests import put

response = put('http://localhost:5002/dateslash', data={'date': '02202025'})
status = response.status_code
data = response.json()
if status == 200:
    print(data['date_slash'])
else:
    print("An error occurred: ", data['error'])