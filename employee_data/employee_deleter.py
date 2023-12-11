# from firebase_admin import initialize_app, db, credentials
#
# cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKey.json')
# firebase_app = initialize_app(cred, {
#     'databaseURL': 'https://orderingsystem-dbe5b.firebaseio.com'
# })

# Your firebase configuration here
firebase_config = {
    # Your config data
}

initialize_app(firebase_config)

def delete_employee(id):
    employee_ref = db.reference('employees').child(id)
    employee_data = employee_ref.get()

    if employee_data:
        employee_ref.delete()
        return True
    else:
        return False

if __name__ == '__main__':
    delete_employee('12345')