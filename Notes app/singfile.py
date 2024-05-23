from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os, json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

# Home route
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        notes = load_notes(username)  # Load user's notes
        return render_template('index.html', username=username, notes=notes)
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if os.path.exists('templates/credentials.txt'):
            with open('templates/credentials.txt', 'r') as file:
                credentials = file.readlines()
                for cred in credentials:
                    stored_username, stored_password = cred.strip().split(' : ')
                    if username == stored_username and check_password_hash(stored_password, password):
                        session['username'] = username
                        return redirect(url_for('home'))

        error = 'Invalid credentials. Please try again.'
        return render_template('login.html', error=error)
    
    return render_template('login.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if os.path.exists('templates/credentials.txt'):
            with open('templates/credentials.txt', 'r') as file:
                credentials = file.read()
                if username in credentials:
                    error = 'Username already exists. Please choose a different username.'
                    return render_template('signup.html', error=error)
        
        hashed_password = generate_password_hash(password)
        with open('templates/credentials.txt', 'a') as file:
            file.write(f'{username} : {hashed_password}\n')
        session['username'] = username
        create_notes_file(username)  # Create a file to store user's notes
        return redirect(url_for('home'))
    
    return render_template('signup.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Rest of the code...


def save_note(username, note):
    filename = f'templates/notes_{username}.txt'
    with open(filename, 'a') as file:
        file.write(f'{note}\n')
def create_notes_file(username):
    filename = f'templates/notes_{username}.txt'
    with open(filename, 'w') as file:
        pass

# Create note route
@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    # Existing code for creating a note
    if request.method == 'POST':
        note = request.form['note']
        username = session['username']
        save_note(username, note)  # Save the note to the user's file
        return redirect(url_for('home'))
    return render_template('create_note.html')


# Helper function to save user's notes to file
def save_notes(username, notes):
    filename = f'notes_{username}.json'
    with open(filename, 'w') as file:
        json.dump(notes, file)

# Helper function to load user's notes from file
def load_notes(username):
    filename = f'notes_{username}.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notes = json.load(file)
        return notes
    return []

# ...

# Create note route
@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        note = request.form['note']
        username = session['username']
        notes = load_notes(username)  # Load user's notes
        notes.append(note)  # Add the new note
        save_notes(username, notes)  # Save the updated notes to file
        return redirect(url_for('home'))
    return render_template('create_note.html')

# Delete note route
@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 'username' in session:
        username = session['username']
        notes = load_notes(username)  # Load user's notes

        # Check if the note_id is valid
        if note_id >= 0 and note_id < len(notes):
            del notes[note_id]  # Delete the note from the list
            save_notes(username, notes)  # Save the updated notes to file

        return redirect(url_for('home'))

    return redirect(url_for('login'))
# Error handler for 404 page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
