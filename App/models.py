from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def __init__(self, username, password):
    self.username= username
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)
    
class Student(db.Model):
  id = db.Column(db.String(9), primary_key=True)

  
class Course(db.Model):
  code = db.Column(db.String(9), primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  students = db.relationship('StudentCourse', backref='course', lazy=True)

  

class StudentCourse(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.String(9), db.ForeignKey('student.id'), nullable=False)
  course_code = db.Column(db.String(9), db.ForeignKey('course.code'), nullable=False)
  student = db.relationship('Student', backref=db.backref('student_courses', lazy=True))


