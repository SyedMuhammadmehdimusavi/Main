from flask import Flask, render_template, request , redirect ,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/students'

db=SQLAlchemy(app)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  first_name=db.Column(db.String(40))
  last_name=db.Column(db.String(40))
  email= db.Column(db.String(40))
  password=db.Column(db.String(40))
  gender=db.Column(db.String(40))
  birthday=db.Column(db.String(40))
  city=db.Column(db.String(40))


  
  def __init__(self,first_name,last_name,email,password,gender,birthday,city):
    self.first_name=first_name
    self.last_name=last_name
    self.email=email
    self.password=password
    self.gender=gender
    self.birthday=birthday
    self.city=city


@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/signup')
# def signup():
#   return render_template('signup.html')



@app.route('/navbar')
def navbar():
  return render_template('navbar.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
  if request.method == 'GET':
      return render_template("signup.html")
  elif request.method == 'POST':
    first_name= request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    password=request.form['password']
    gender=request.form['gender']
    birthday=request.form['birthday']
    city=request.form['city']


  student=Student(first_name,last_name,email,password,gender,city,birthday)
  db.session.add(student)
  db.session.commit()

  #fetch a certain student2
  studentResult=db.session.query(Student).filter(Student.id==1)
  for result in studentResult:
    print(result.first_name)

  return render_template('signin.html', data=first_name)



@app.route('/signin')
def signin():
  return render_template('signin.html')


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)


# open pyAdmin4 
# create new Database like nae -> students
# run  -> python
# Then run -> from app import db
# db.create_all() 


