from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

# Sample users
users = {'livvyas': User('livvyas'), 'john': User('john')}

# User Loader
@login_manager.user_loader
def load_user(username):
    return users.get(username)

# Routes
@app.route('/')
def home():
    return redirect(url_for('login')) 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            user = User(username)
            users[username] = user
            login_user(user)
            return redirect(url_for('notes'))
        return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and password == 'pass123':
            login_user(user)
            return redirect(url_for('notes'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
