import cv2
from datetime import datetime
from firebase_admin import db

timelimit = 15


def check_employee_name(qr_code_data):
    qr_code_parts = ""
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
                datetimeObject = datetime.strptime(employee['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

                if secondsElapsed > timelimit:
                    total = employee.get('total_attendance', 0) + 1
                    employees_ref.child(qr_id).update({
                        'total_attendance': total,
                        'last_attendance_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print("Attendance Updated!")

                return True
        return True


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

if __name__ == "__main__":
    check_qr_codes_from_camera()
