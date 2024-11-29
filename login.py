from flask import Flask, Blueprint, request, redirect, url_for, render_template
import sqlite3

login_bp = Blueprint("login", __name__)
def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def check_user(name, pw):
    # Get database connection
    print("check user")
    conn = get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    cur.execute('SELECT userName, userPW FROM users WHERE userName = ?', (name,))    
    # First row returned (should be only)
    row = cur.fetchone()
    print(row[0])
    print(row[1])
    # Close connection
    conn.close()
    # Nothing returned - user not found
    if row is None: 
        # user not found
        print("User name not found")
    # Username found but password doesn't match
    elif row[1] != pw:
        # invalid password
        print("Invalid password")
    # Both match - successful login
    else:
        print("Successful login")
        return True
       
    return False

@login_bp.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_user(username, password):
        #if username == "user" and password == "1234":
            import userStore
            userStore.set_user(username)
            return redirect(url_for("home.home"))  # Redirect to the home page
        else:
            userStore.set_user("")
            message = "Incorrect Username or Password."

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Screen</title>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="text-align: center; width: 500px; font-family: fantasy">
            <h1>Limitless</h1>
            <form method="POST">
                <div style="font-family: sans-serif">
                    <label>Username/Email:</label>
                    <input type="text" name="username" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Password:</label>
                    <input type="password" name="password" required>
                </div>
                <div style="margin-top: 20px; font-family: sans-serif">
                    <button type="submit">Login</button>
                </div>
            </form>
            <div style="margin-top: 15px; color: blue; text-decoration: underline;">
                <a href="./register">Create an account</a>
            </div>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """
    return html
