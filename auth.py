from sqlite3 import IntegrityError
from registrations.build_app import db
import bcrypt
from API.Project.models import User
from app import app
from flask import Flask, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
app.config['JWT_SECRET_KEY'] = 'c3fc3fbba4ee4dac948e238c9b8df699'


@app.route('/register', methods=['POST'])
def register():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(email=email, hash=hashed)
        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity={"email": email})
        return {"access_token": access_token}, 200
    except IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400