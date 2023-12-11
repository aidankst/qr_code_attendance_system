from employee_creation import add_employee
from employee_checker import verify_employee_data
from employee_deleter import delete_employee

from firebase_admin import initialize_app, db, credentials

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
            case '2': verify_employee_data()
            case '3': delete_employee()
            case '4': condition = False

if __name__ == "__main__":
    initiator()