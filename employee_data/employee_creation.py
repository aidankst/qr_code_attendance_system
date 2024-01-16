import os
import qrcode
from firebase_admin import db

def add_employee(name, id, position):

    while True:

        employee_data = {
            'name': name,
            'id': id,
            'position': position,
            'last_attendance_time': "2022-01-01 12:00:00",
            'total_attendance': 0
        }
        employee_ref = db.reference('employees').child(id)
        employee_ref.set(employee_data)

        qr_code_path = os.path.join(os.path.dirname(__file__), 'employee_data', 'static', 'qr_codes', f'{id}.png')
        img = qrcode.make(f'{id}, {name}, {position}')
        img.save(qr_code_path)

        print("Employee data has been saved to database.")