from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

def validate_date(date_str):

    # Check that date is digit
    if not date_str.isdigit():
        return False, {'error': 'Date must contain only digits (MMDDYYYY).'}
    # Check that date is correct length
    if len(date_str) != 8:
        return False, {'error': 'Date is incorrect length.'}
    # Check that month is valid
    date_month = date_str[:2]
    if not '01' <= date_month <= '12':
        return False, {'error': 'Month is invalid.'}
    # Check that day is valid
    date_day = date_str[2:4]
    if not '01' <= date_day <= '31':
        return False, {'error': 'Day is invalid.'}
    # Check that year is valid
    date_year = date_str[4:]
    if not '1900' <= date_year <= '2026':
        return False, {'error': 'Year is invalid.'}
    
    # Complete Date Validation
    try:
        weekday = datetime.strptime(date_str, "%m%d%Y")
    except ValueError:
        return False, {'error': 'Date is not a real calendar date.'}


    # Date is valid, return parsed date
    return True, {
        'date_month': date_month, 
        'date_day': date_day, 
        'date_year': date_year,
        'weekday': weekday # 
        }

class DateSlash(Resource):
    def put(self):
        # Get date string from the request
        date = request.form['date']
        # Validate the date that was sent
        validate_result, validate_msg = validate_date(date)
        # If invalid, return with error msg and code 400
        if not validate_result:
            return validate_msg, 400
        # Date is valid, generate string with slashes and return
        date_slash = validate_msg['date_month'] + '/' + validate_msg['date_day'] + '/' + validate_msg['date_year']
        return {'date_slash': date_slash}

class DayOfWeek(Resource):
    def put(self):
        # Get date string from the request
        date = request.form['date']
        # Validate the date
        validate_result, validate_msg = validate_date(date)
        # If invalid, return error msg
        if not validate_result:
            return validate_msg, 400
        # Parse data and retrieve day of the week
        weekday = validate_msg['weekday']
        day_name = weekday.strftime("%A")

        return {'day_of_week': day_name}


api.add_resource(DateSlash, '/dateslash')
api.add_resource(DayOfWeek,'/dayofweek')

if __name__ == "__main__":
    app.run(port=5002)