from requests import put

date_input = '02202025'

date_response = put('http://localhost:5002/dateslash', data={'date': date_input})
day_response  = put('http://localhost:5002/dayofweek', data={'date': date_input})

# Date (Slash Format)
if date_response.status_code == 200:
    print("Slash format:", date_response.json()['date_slash'])
else:
    print("Slash error:", date_response.json()['error'])

# Day of the week
if day_response.status_code == 200:
    print("Day of week:", day_response.json()['day_of_week'])
else:
    print("Day error:", day_response.json()['error'])