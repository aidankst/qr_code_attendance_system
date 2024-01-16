from employee_creation import add_employee
from employee_checker import check_qr_codes_from_camera, check_employee_name
from employee_deleter import delete_employee
from firebase_admin import initialize_app, credentials
from flask import Flask, flash, redirect, render_template, request, jsonify

app = Flask(__name__)

cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKeyUpdated.json')
firebase_app = initialize_app(cred, {
    'databaseURL': 'https://employee-attendance-syst-4e7a6-default-rtdb.firebaseio.com'
})


def initiator():
    condition = True

    while condition:
        temp = input ("Choose the input \n 1. Employee Creator \n 2. Employee Checker \n 3. Employee Deleter \n 4. quit\n " )
        
        match temp:
            case '1': add_employee("Kaung Sithu", "414175", "Manager")
            case '2': check_qr_codes_from_camera()
            case '3': delete_employee()
            case '4': condition = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_employee', methods=['GET'])
def create_employee():
    name = request.form.get('name')
    id = request.form.get('id')
    position = request.form.get('position')
    if name and id and position:  # Check if name, id, and position are not None
        add_employee(name, id, position)
    else:
        return "Error: Missing form data", 400  # Return an error response
    return render_template('create_employee.html')

@app.route('/check_employee', methods=['GET'])
def check_employee():
    data = request.get_json()
    qr_code_data = data.get('qr_code_data')
    attendance = check_employee_name(qr_code_data)
    return jsonify({"attendance": attendance})
    # return render_template('check_employee.html')

@app.route('/delete_employee', methods=['GET'])
def remove_employee():
    try:
        employee_id = request.args.get("employee_id")
        result = delete_employee(employee_id)
        # return jsonify({'success': True, 'result': result})
        return render_template('delete_employee.html')
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
    # initiator()