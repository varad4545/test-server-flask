from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}@localhost:5432/{os.getenv('DB_NAME')}"

app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models
from models.student import Student

@app.route('/create-user', methods=['POST'])
def create_user():
  body = request.get_json()
  student = Student(body['name'], body['email'])
  db.session.add(student)
  db.session.commit()
  return "item created"

if __name__ == "__main__":
    app.run(debug=True)