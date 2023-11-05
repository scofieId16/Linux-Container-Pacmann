from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Edit disini
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty123@172.25.0.3/pgproject'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

@app.route("/", methods=['GET', 'POST'])
def signup_form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        user = Users(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect("/signup")
    
    return render_template("signup_form.html")

@app.route("/signup")
def signup():
    users = Users.query.all()
    return render_template("signup.html", users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    

