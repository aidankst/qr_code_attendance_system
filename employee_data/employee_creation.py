import os
import qrcode
from firebase_admin import db

# cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKey.json')
# firebase_app = initialize_app(cred, {
#     'databaseURL': 'https://orderingsystem-dbe5b.firebaseio.com'
# })

def add_employee():

    while True:
        name = input("Enter employee name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        id = input("Enter employee ID: ")
        position = input("Enter employee position: ")

        employee_data = {
            'name': name,
            'id': id,
            'position': position,
            'attendance': []
        }
        employee_ref = db.reference('employees').child(id)
        employee_ref.set(employee_data)

        # Create qr code
        if not os.path.exists('qr_codes'):
            os.mkdir('qr_codes')
        img = qrcode.make(f'{id}, {name}, {position}')
        img.save(f'/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/qr_codes/{id}.png')

        print("Employee data has been saved to database.")

# if __name__ == '__main__':
#     # add_employee('John Doe', '12345', 'Software Engineer')
#     add_employee()