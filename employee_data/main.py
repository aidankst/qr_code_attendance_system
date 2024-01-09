from employee_creation import add_employee
from employee_checker import check_qr_codes_from_camera, check_employee_name
from employee_deleter import delete_employee
from firebase_admin import initialize_app, credentials
from flask import Flask, flash, redirect, render_template, request, jsonify

app = Flask(__name__)

cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKey.json')
firebase_app = initialize_app(cred, {
    'databaseURL': 'https://orderingsystem-dbe5b-default-rtdb.europe-west1.firebasedatabase.app'
})


def initiator():
    condition = True

    while condition:
        temp = input ("Choose the input \n 1. Employee Creator \n 2. Employee Checker \n 3. Employee Deleter \n 4. quit\n " )
        
        match temp:
            case '1': add_employee()
            case '2': check_qr_codes_from_camera()
            case '3': delete_employee()
            case '4': condition = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_employee', methods=['POST'])
def create_employee():
    name = request.form['name']
    id = request.form['id']
    position = request.form['position']
    add_employee(name, id, position)
    return jsonify({"message": "Employee created successfully"})

@app.route('/check_employee', methods=['POST'])
def check_employee():
    qr_code_data = request.form['qr_code_data']
    attendance = check_employee_name(qr_code_data)
    return jsonify({"attendance": attendance})

@app.route('/delete_employee', methods=['POST'])
def remove_employee():
    employee_id = request.form['id']
    delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)