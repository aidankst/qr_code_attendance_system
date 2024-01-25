# QR Code Attendance System

*  **By**: Edibe Tutku Gayda, Min Khant, Małgorzata Kuczera, Kaung Sithu
*  ***AGH University of Science and Technology***
*  Software Studio II Project

## Overview

The QR Attendance System is an innovative and comprehensive solution designed to streamline employee attendance tracking through the use of QR codes. This system integrates various technologies, including a Flask web application, Firebase Realtime Database, and computer vision capabilities, to provide an efficient and user-friendly attendance management platform.
## Key Features

- Effortless Employee Record Creation: Seamlessly create and manage employee records with their respective names, IDs, and positions.

- Streamlined Attendance Tracking: Utilize an integrated QR code scanner to effortlessly check employee attendance, eliminating manual attendance sheets or time tracking systems.

- Seamless Employee Record Deletion: Efficiently remove employee records from the system when necessary.

## Core Technologies

- Python: The foundational programming language ensuring stability and reliability.

- Flask: The robust web framework orchestrating the application's user interface and data handling.

- Firebase Realtime Database: The highly secure and scalable NoSQL database storing employee data securely and reliably.

- jsQR: The lightweight JavaScript library enabling efficient QR code decoding from the camera feed.

## Implementation Architecture

The application's core components are organized as follows:

- `main.py`: The application's entry point, initializing Flask and Firebase connections.

- `employee_creation.py`: Handles employee record creation, including QR code generation.

- `employee_checker.py`: Scans camera feed, decodes QR codes, and verifies attendance against existing records.

- `employee_deleter.py`: Removes employee records from the Firebase database.

- `HTML Templates (index.html, create_employee.html, check_employee.html, delete_employee.html)`: rovides the user interface, including various functionalities like employee creation, checking, and deletion.

## Deployment Options

The system is designed for deployment on web servers or cloud platforms, offering flexible accessibility options.

## Testing Methodology

1. **Record Management**: Testing involved verifying the creation and deletion of employee records to ensure accurate database interactions.
2. **QR Code Scanning and Attendance Tracking**: Focused on evaluating the precision of QR code scanning and the effectiveness of the attendance tracking mechanism.

## Safety and Security Analysis

### Data Management
- Uses Firebase Realtime Database, implying a focus on secure data storage. However, the effectiveness depends on the implementation of security rules and authentication methods.

### Application Security
- Flask's built-in security features must be correctly configured for robust protection.
- Security measures in QR code processing are vital to prevent data breaches.

### Deployment Security
- Adherence to standard web application security practices, including the use of HTTPS and secure authentication, is essential for safe deployment.

### Best Practices and Code Quality
- The project's adherence to Python and Flask best practices significantly affects the system's security and maintainability.

### Potential Vulnerabilities
- The system's vulnerability to external threats depends on factors like server security, code robustness, and security measures in database management.


## Getting Started
1. Ensure Python is installed on your machine.
2. Install the required Python packages.
3. Execute main.py to launch the Flask web application.
4. Open a web browser and navigate to [http://localhost:5000/](http://127.0.0.1:5000) to access the QR Attendance System.

## Conclusion

The QR Code Attendance System empowers organizations to streamline employee management operations, enhance attendance tracking, and maintain accurate employee data. With its robust architecture, seamless user interface, and adherence to industry best practices, this project serves as a valuable tool for businesses seeking to optimize their employee management operations.
