from requests import put

tests = [
    "02202025",  # normal
    "02292024",  # leap day valid
    "02292025",  # leap day invalid
    "04312025",  # invalid calendar date
    "13202025",  # bad month
    "02AA2025",  # non-digit
]

if __name__ == "__main__":
    for t in tests:
        print("\nCurrent Test:", t)
        date_response = put('http://localhost:5002/dateslash', data={'date': t})
        day_response  = put('http://localhost:5002/dayofweek', data={'date': t})
        print("Date Slash:", date_response.status_code, date_response.json())
        print("Day of Week:", day_response.status_code, day_response.json())