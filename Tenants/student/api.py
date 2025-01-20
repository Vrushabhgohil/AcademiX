from flask import Blueprint, render_template


student_api = Blueprint('student_api', __name__,
                      template_folder='Templates', static_folder='static')

@student_api.route('/student_login', methods=['GET'])
def student_login():
    return render_template('login_student.html')
@student_api.route('/student_signup', methods=['GET'])
def student_signup():
    return render_template('signup_student.html')
@student_api.route('/student_home', methods=['GET'])
def student_home():
    return render_template('student-home.html')