import datetime
import cv2
from firebase_admin import db

# cred = credentials.Certificate("/path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "https://your-project-id.firebaseio.com/"
# })

timelimit=15

def decode_qr_code(image):
    # Initialize the QR code decoder
    qr_decoder = cv2.QRCodeDetector()

    # Define a ROI (Region of Interest) to focus the search for QR codes
    roi = image[200:300, 300:400]

    gray_roi = None
    # Check if the ROI is empty before converting it to grayscale
    if roi is None or roi.size == 0:
        # Handle the empty ROI
        print("Empty ROI detected.")
    else:
        # Check if the input image has three channels before converting it to grayscale
        if roi.ndim != 3:
            # Handle the multi-channel image
            print("Input image has more than three channels.")
        else:
            # Convert the ROI to grayscale
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Iterate through the ROI pixels to find QR codes
        for x in range(gray_roi.shape[1]):
            for y in range(gray_roi.shape[0]):
            # Check if the current pixel value indicates a QR code module
                if gray_roi[y, x] == 0:
                # If a QR code module is detected, try decoding the QR code data
                    potential_qr_code = gray_roi[y-2:y+3, x-2:x+3]
                    if qr_decoder.decode(potential_qr_code):
                    # Extract the decoded QR code data
                        decoded_text = qr_decoder.decode_data(potential_qr_code).decode('utf-8').split(',')
                        return decoded_text

def update_attendance(employee_data):
    # Split the employee data into parts
    employee_id = employee_data[0]

    # Get the employee data from the firebase database
    employeeinfo = db.reference(f"Employees/{employee_id}").get()
    ref = db.reference(f"Employees/{employee_id}")

    datetimeObject = datetime.strptime(employeeinfo['last_attendance_time'],
                                       "%Y-%m-%d %H:%M:%S")
    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

    if secondsElapsed > timelimit:
        total = employeeinfo['total_attendance'] + 1
        ref.child('total_attendance').set(total)
        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def verify_employee_data():
    # Start capturing the camera feed
    camera = cv2.VideoCapture(0)

    while True:
        # Capture each frame
        ret, frame = camera.read()

        # Get the ROI for the QR code detection
        roi = frame[200:300, 300:400]

        # Convert the ROI to grayscale
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Check for QR codes within the ROI
        employee_data = decode_qr_code(gray_roi)

        # Update attendance if the employee is verified
        if employee_data:
            for decoded_text in employee_data:
                update_attendance(decoded_text)
                print("Attendance marked successfully for employee ID:", decoded_text[0])

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Stop the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the output window
    camera.release()
    cv2.destroyAllWindows()
