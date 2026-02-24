# Date Format Microservice (Flask REST)

A REST API based microservice that accepts a date in **MMDDYYYY** format and returns:
1) The same date in **MM/DD/YYYY** format, and/or  
2) The **day of the week** for the given date (e.g., "Thursday").

It performs input validation (digits only, correct length, valid month/day/year range, and real calendar date including leap years).

---

## Requirements
- Python 3.9+
- Flask
- requests

## Communication Contract

### Base URL
- Default (local): `http://localhost:5002`

### Data Format
- Requests send the date as **x-www-form-urlencoded** form data
- Body key: `date`
- Date must be a string in the format: `MMDDYYYY`

Example:
- `02202025` → 02/20/2025

---

## Requests

### Example Request (dateslash)

```python
from requests import put

response = put(
    "http://localhost:5002/dateslash",
    data={"date": "02202025"}
)

print(response.status_code)
print(response.json())
```

### Example Request (dayofweek)

```python
from requests import put

response = put(
    "http://localhost:5002/dayofweek",
    data={"date": "02202025"}
)

print(response.status_code)
print(response.json())
```
---

### Example Response

```python
if slash_response.status_code == 200:
    print("Slash format:", slash_response.json()["date_slash"])
else:
    print("Error:", slash_response.json()["error"])

if dow_response.status_code == 200:
    print("Day of week:", dow_response.json()["day_of_week"])
else:
    print("Error:", dow_response.json()["error"])
```

---

# Running the Microservice

Step 1 - Install dependencies

```
pip install flask flask-restful requests
```

Step 2 - Run on the CLI

```
python date_format_api.py
```

The service will auto start on:

http://localhost:5002


---

# Example Client

Run the provided client:

```
python date_format_client.py
```

---

# UML