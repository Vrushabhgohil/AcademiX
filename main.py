from flask import Flask, render_template, request, jsonify
from Tenants.student.api import student_api
from Tenants.tutors.api import tutor_api


app = Flask(__name__)
app.register_blueprint(student_api)
app.register_blueprint(tutor_api)
@app.route('/welcome')
def default():     
    return render_template('Default.html')

if __name__ == '__main__':
    app.run(debug=True)