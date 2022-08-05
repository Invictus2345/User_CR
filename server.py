
from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')
def index():
    allusers = User.get_all_users()
    return render_template('index.html', users = allusers)

@app.route('/users', methods=['POST'])
def users():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/all')
def all():
    allusers = User.get_all_users()
    return render_template('allusers.html', users=allusers)


if __name__ == "__main__":
    app.run(debug=True)