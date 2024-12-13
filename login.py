from flask import Flask, Blueprint, request, redirect, url_for, render_template
import sqlite3

import database

login_bp = Blueprint("login", __name__)

def check_user(name, pw):
    # Get database connection
    conn = database.get_db_connection()

def check_user(name, pw):
    # Get database connection
    conn = database.get_db_connection()

    # Create cursor and run select to look for username
    cur = conn.cursor()
    cur.execute('SELECT userName, userPW FROM users WHERE userName = ?', (name,))    
    # First row returned (should be only)
    row = cur.fetchone()
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

        import userStore
        if check_user(username, password):
        #if username == "user" and password == "1234":
            userStore.set_user(username)
            # Get user's current weight and store in User Store
            weight = database.get_Weight_from_db(username)
            userStore.set_weight(weight)
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
<body style="margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: Arial, sans-serif; background: linear-gradient(to bottom, #6fb1fc, #add8e6);">


        <img src="data:image/png;base64,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" alt="Person Working Out" style="width: 150px; height: 150px; margin-bottom: 20px;">

            
            <div style="text-align: center; width: 500px; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <!-- Title -->
                <h1 style="font-size: 64px; color: white; text-shadow: 2px 2px 5px #000; margin-bottom: 20px;">Limitless</h1>

                <!-- Form -->
                <form method="POST">
                    <div>
                        <label for="username" style="display: block; margin-bottom: 5px; font-weight: bold;">Username/Email:</label>
                        <input type="text" id="username" name="username" required style="width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
                    </div>
                    <div style="margin-top: 10px;">
                        <label for="password" style="display: block; margin-bottom: 5px; font-weight: bold;">Password:</label>
                        <input type="password" id="password" name="password" required style="width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
                    </div>
                    <div>
                        <button type="submit" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 15px;">Login</button>
                    </div>
                </form>

                <!-- Link -->
                <div style="margin-top: 15px;">
                    <a href="./register" style="color: #007bff; text-decoration: none;">Create an account</a>
                </div>
            </div>


        </body>
        </html>
    """
    return html