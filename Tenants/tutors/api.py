from flask import Blueprint, render_template


tutor_api = Blueprint('tutor_api', __name__,
                      template_folder='Templates', static_folder='static')

@tutor_api.route('/tutor_login', methods=['GET'])
def tutor_login():
    return render_template('login_tutor.html')
@tutor_api.route('/tutor_signup', methods=['GET'])
def tutor_signup():
    return render_template('request_tutor.html')
@tutor_api.route('/tutor_home', methods=['GET'])
def tutor_home():
    return render_template('tutor-home.html')