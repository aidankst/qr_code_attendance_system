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

- `HTML Templates (index.html, create_employee.html, check_employee.html, delete_employee.html)`: Define the application's user interface.

## Deployment Options

The application can be deployed to a web server or cloud platform for user access.

## Getting Started
1. Ensure Python is installed on your machine.
2. Install the required Python packages.
3. Execute main.py to launch the Flask web application.
4. Open a web browser and navigate to [http://localhost:5000/](http://127.0.0.1:5000) to access the QR Attendance System.

## Testing Methodology

- Verify the creation and deletion of employee records.

- Test the accuracy of QR code scanning and attendance tracking.

## Conclusion

The QR Code Attendance System empowers organizations to streamline employee management operations, enhance attendance tracking, and maintain accurate employee data. With its robust architecture, seamless user interface, and adherence to industry best practices, this project serves as a valuable tool for businesses seeking to optimize their employee management operations.
