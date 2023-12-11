import cv2
# from firebase_admin import credentials, db, initialize_app
#
# cred = credentials.Certificate('/Users/sithukaung/Library/CloudStorage/GoogleDrive-aidan.kst@icloud.com/My Drive/AGH/5th Semester/Software Studio/QR Attendance/employee_data/serviceAccountKey.json')
# firebase_app = initialize_app(cred, {
#     'databaseURL': 'https://orderingsystem-dbe5b.firebaseio.com'
# })

def decode_qr_code(image):
    # Define the QR code detection parameters
    qr_decoder = cv2.QRCodeDetector()

    # Find all potential QR codes in the image
    results = qr_decoder.detectMultiScale(image, None, 1.1, 2)

    # Extract the employee data from the first detected QR code
    if results:
        # Get the bounding box coordinates of the QR code
        (x, y, w, h) = results[0]

        # Extract the QR code data
        decoded_text = qr_decoder.decode_data(image[y:y+h, x:x+w])
        employee_data = decoded_text.decode('utf-8')
        return employee_data
    else:
        return None

def verify_employee_data(employee_data):
    # Split the employee data into parts
    employee_id, employee_name, employee_position = employee_data.split(',')

    # Connect to the firebase database
    database = db.reference()

    # Get the employee data from the firebase database
    employee_info = database.child('employees').child(employee_id).get()

    if employee_info:
        # Compare the employee data with the firebase database
        if (employee_info['name'] == employee_name) and (employee_info['position'] == employee_position):
            return True
        else:
            return False
    else:
        return False

# Start capturing the camera feed
cap = cv2.VideoCapture(0)

while True:
    # Capture each frame
    ret, frame = cap.read()

    # Apply grayscale conversion for QR code detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode the QR code from the frame
    employee_data = decode_qr_code(gray)

    if employee_data:
        # Verify the employee data with the firebase database
        if verify_employee_data(employee_data):
            print("Employee verified successfully!")
        else:
            print("Invalid employee data!")

    # Display the frame
    cv2.imshow('Employee Verification', frame)

    # Stop the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the output window
cap.release()
cv2.destroyAllWindows()
