from flask import Flask
from faculty.faculty import faculty_var
from student.student import student_var

if __name__ == '__main__':
    app = Flask(__name__)
    print("starting flask app...")
    app.register_blueprint(faculty_var)
    app.register_blueprint(student_var)
    app.run(debug=True)






