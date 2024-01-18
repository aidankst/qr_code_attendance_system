from firebase_admin import db

def delete_employee(employee_id):
    try:
        employee_ref = db.reference('employees').child(employee_id)
        employee_data = employee_ref.get()

        if employee_data:
            employee_ref.delete()
            return print(f"Employee with ID {employee_id} has been deleted.")
        else:
            print(f"The employee with ID {employee_id} does not exist.")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
