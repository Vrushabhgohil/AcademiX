from flask import Flask, render_template
from common.extension import db  
from Tenants.student.api import student_api
from Tenants.tutors.api import tutor_api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///academiX.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(student_api, url_prefix='/student')
    app.register_blueprint(tutor_api, url_prefix='/tutor')

    @app.route('/welcome')
    def default():
        return render_template('Default.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
