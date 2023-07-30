from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random string

# Simulation de base de données d'utilisateurs (utilisez une vraie base de données en production)
users = {
    'john': {'password': 'johnspassword'},
    'mary': {'password': 'maryspassword'}
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        flash(f'Vous êtes connecté en tant que {username}', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Identifiants incorrects. Veuillez réessayer.', 'error')
        return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    return "Bienvenue dans votre espace utilisateur."


if __name__ == '__main__':
    app.run(debug=True)
