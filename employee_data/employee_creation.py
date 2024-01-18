import os
import qrcode
from firebase_admin import db

def add_employee(name, id, position):

    employee_data = {
        'name': name,
        'id': id,
        'position': position,
        'last_attendance_time': "2023-01-01 12:00:00",
        'total_attendance': 0
    }
    employee_ref = db.reference('employees').child(id)
    employee_ref.set(employee_data)

        # qr_code_path = os.path.join(os.path.dirname(__file__), 'employee_data', 'static', 'qr_codes', f'{id}.png')
    img = qrcode.make(f'{id}, {name}, {position}')
    img.save(f'/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/static/qr_codes/{id}.png')

    print("Employee data has been saved to database.")

if __name__ == '__main__':
    while True:
        name = input("Enter employee name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        id = input("Enter employee ID: ")
        position = input("Enter employee position: ")

    add_employee(name, id, position)