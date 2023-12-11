import cv2
from datetime import datetime
from firebase_admin import db

timelimit = 15
def check_employee_name(qr_code_data):
    # Assuming the database structure is '/employees/{employee_id}'
    employees_ref = db.reference('employees')

    for employee_id in employees_ref.get():
        employee = employees_ref.child(employee_id).get()
        stored_name = employee.get('name', '').strip().lower()

        # Extract name from QR code data
        qr_code_lines = qr_code_data.split('\n')
        if len(qr_code_lines) > 0:
            qr_code_name_parts = qr_code_lines[0].split(': ')
            if len(qr_code_name_parts) > 1:
                qr_code_name = qr_code_name_parts[1].strip().lower()

                if stored_name == qr_code_name:
                    datetimeObject = datetime.strptime(employee['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

                    if secondsElapsed > timelimit:
                        total = employee.get('total_attendance', 0) + 1
                        employees_ref.child(employee_id).update({
                            'attendance': total,
                            'last_attendance_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

                    return True

    return False

def check_qr_codes_from_camera():
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera
    qr_detector = cv2.QRCodeDetector()

    while True:
        ret, frame = camera.read()

        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            retval, decoded_info, _, _ = qr_detector.detectAndDecodeMulti(gray_frame)

            if retval:
                for qr_code_data in decoded_info:
                    qr_code_data = qr_code_data.strip()
                    print(f"QR Code Data: {qr_code_data}")

                    is_employee = check_employee_name(qr_code_data)

                    if is_employee:
                        print("The QR code corresponds to an employee in the Firebase database.")
                    else:
                        print("The QR code does not match any employee in the Firebase database.")

            cv2.imshow("QR Code Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()


