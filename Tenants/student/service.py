import uuid

from flask import request


def Student_signup():
    id = uuid.uuid4()
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    dob = request.form.get('dob')

    sql = 'insert into Student (id, name, email,phone,dob) values'