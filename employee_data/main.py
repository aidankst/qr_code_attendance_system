from employee_creation import add_employee
from employee_checker import check_qr_codes_from_camera, check_employee_name
from employee_deleter import delete_employee
from firebase_admin import initialize_app, credentials, db
from flask import Flask, flash, redirect, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

cred = credentials.Certificate('employee_data/serviceAccountKeyUpdated.json')
firebase_app = initialize_app(cred, {
    'databaseURL': 'https://employee-attendance-syst-4e7a6-default-rtdb.firebaseio.com' 
})

timelimit = 15
def initiator():
    condition = True

    while condition:
        temp = input ("Choose the input \n 1. Employee Creator \n 2. Employee Checker \n 3. Employee Deleter \n 4. quit\n " )
        
        match temp:
            case '1': add_employee("Min", "003", "Student")
            case '2': check_qr_codes_from_camera()
            case '3': delete_employee()
            case '4': condition = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_employee', methods=['GET'])
def create_employee():
    try:
        name = request.args.get('name')
        id = request.args.get('id')
        position = request.args.get('position')
        if name and id and position:  # Check if name, id, and position are not None
            add_employee(name, id, position)
        elif name:
            return "Error: Only name present"
        elif id:
            return "Error: Only id present"
        elif position:
            return "Error: Only position present"
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    return render_template('/create_employee.html')

@app.route('/check_employee', methods=['POST', 'GET'])
def check_employee():
    qr_code_data = request.args.get('qr_code_data')
    
    if qr_code_data:
        qr_code_parts = qr_code_data.split(', ')
        if len(qr_code_parts) == 3:
            qr_id, qr_name, qr_position = qr_code_parts
            qr_id = qr_id.strip()

            employees_ref = db.reference('employees')
            employee = employees_ref.child(qr_id).get()

            if employee:
                stored_name = employee.get('name', '').strip().lower()
                stored_position = employee.get('position', '').strip().lower()

                print(f"QR ID: {qr_id}, QR Name: {qr_name}, QR Position: {qr_position}")
                print(f"Stored Name: {stored_name}, Stored Position: {stored_position}")

                if 'last_attendance_time' in employee:
                    datetime_object = datetime.strptime(employee['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                    seconds_elapsed = (datetime.now() - datetime_object).total_seconds()

                    if seconds_elapsed > timelimit:
                        total = employee.get('total_attendance', 0) + 1
                        employees_ref.child(qr_id).update({
                            'total_attendance': total,
                            'last_attendance_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        return jsonify({'is_employee': True, 'message': 'Attendance Updated!'})
                    else:
                        return jsonify({'is_employee': True, 'message': 'Attendance not updated. Time limit not reached.'})
                else:
                    return jsonify({'is_employee': True, 'message': 'Employee has no attendance record.'})
            else:
                return jsonify({'is_employee': False, 'message': 'QR code does not match any employee in the database.'})

    return render_template('/check_employee.html')


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