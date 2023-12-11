from firebase_admin import db
#
# cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKey.json')
# firebase_app = initialize_app(cred, {
#     'databaseURL': 'https://orderingsystem-dbe5b.firebaseio.com'
# })

def delete_employee():
    id = input("Enter the employee id which you would like to delete: ")
    employee_ref = db.reference('employees').child(id)
    employee_data = employee_ref.get()

    if employee_data:
        employee_ref.delete()
        return True
    else:
        return False

if __name__ == '__main__':
    delete_employee('12345')