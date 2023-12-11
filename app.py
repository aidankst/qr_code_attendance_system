# from flask import Flask, render_template, request, redirect, url_for
# import employee_data.employee_creation as employee_creation
# import employee_data.employee_checker as employee_checker
# import employee_data.employee_deleter as employee_deleter
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/create_employee', methods=['POST'])
# def create_employee():
#     name = request.form['name']
#     id = request.form['id']
#     position = request.form['position']
#
#     employee_creation.add_employee(name, id, position)
#
#     return redirect(url_for('home'))
#
# @app.route('/check_employee', methods=['POST'])
# def check_employee():
#     id = request.form['id']
#
#     if employee_checker.check_employee(id):
#         return redirect(url_for('home'))
#     else:
#         return "Employee not found", 404
#
# @app.route('/delete_employee', methods=['POST'])
# def delete_employee():
#     id = request.form['id']
#
#     if employee_deleter.delete_employee(id):
#         return redirect(url_for('home'))
#     else:
#         return "Employee not found", 404
#
# if __name__ == '__main__':
#     app.run(debug=True)