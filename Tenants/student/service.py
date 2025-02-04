import jwt
from flask import jsonify, redirect, request, current_app, url_for
from common.database import Student, session
from common.extension import db  
from datetime import datetime

def Student_signup_data():
    with current_app.app_context():  # Ensure Flask context is active
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        password = request.form.get('password')
        payload = {'password': password}
        token = jwt.encode(payload, 'vrushabh@2611', algorithm='HS256')
        new_passwrod = token
        if not all([name, email, phone, dob,password]):
            return jsonify({'error': 'Missing required fields'}), 400

        try:
            dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

        new_student = Student(
            name=name,
            email=email,
            phone=phone,
            date_birth=dob
        )

        session.add(new_student)
        session.commit()
        return redirect(url_for('student_api.student_home'))

