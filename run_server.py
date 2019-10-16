from flask import Flask
from first_restapi.faculty.faculty import faculty_var
from first_restapi.student.student import student_var

if __name__ == '__main__':
    app = Flask(__name__)
    print("starting flask app...")
    app.register_blueprint(faculty_var)
    app.register_blueprint(student_var)
    app.run(debug=True)






