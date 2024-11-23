from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Login Page Route
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simple check for demonstration (replace with real check later)
        if username == "user" and password == "1234":
            return redirect(url_for("home"))  # Redirect to the home page
        else:
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
                <a href="#">Create an account</a>
            </div>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """
    return html

# Home Page Route
@app.route("/home")
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            ul {{
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }}

            li {{
                float: left;
            }}

            li h2 {{
                display: block;
                color: lightblue;
                text-align: center;
                padding-left: 10px;
                text-decoration: none;
            }}

            li a {{
                display: block;
                color: white;
                text-align: center;
                padding-top: 27px;
                padding-left: 30px;
                text-decoration: none;
            }}

            li a:hover {{
                color: lightblue;
            }}

            .active {{
                color: white;
                padding-right: 14px;
                border-radius: 12px;
            }}

            #achievements-card {{
                border: 2px solid lightblue;
                padding: 50px;
                color: black;
                display: block;
                float: left;
            }}

            #progress-card {{
                border: 2px solid lightblue;
                padding: 50px;
                color: black;
                display: inline-block;
            }}

            #goals-card {{
                border: 2px solid lightblue;
                padding: 50px;
                color: black;
                display: block;
                float: right;
            }}
        
            .cards-container {{
                width: 100%;
                margin: 0 auto;
                display: inline-block;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="#home">Home</a></li>
                <li><a href="#workout">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
                <li style="float:right"><a class="active" href="#account">Account</a></li>
            </ul>
        </nav>

        <div class="container">
            <div class="summary-container">
                <h3>Weekly Summary:</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>

            <div class="cards-container">
                <div id="achievements-card">
                    <h2>Achievements</h2>
                    <p>Badges will go here</p>
                </div>
                <div id="progress-card">
                    <h2>Progress</h2>
                    <p>Progress will go here</p>
                </div>
                <div id="goals-card">
                    <h2>Goals</h2>
                    <p>Goals will go here</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html

# Workout Page Route
@app.route("/workout")
def workout():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Workout Page</title>
        <style>
            /* General Styles */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }

            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            nav li a:hover {
                background-color: lightblue;
                color: black;
            }

            .active {
                background-color: lightskyblue;
                color: black;
            }

            .icon-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                padding: 20px;
                text-align: center;
            }

            .icon {
                background-color: #fff;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 8px;
                transition: transform 0.3s;
            }

            .icon img {
                width: 50px;
                height: 50px;
            }

            .icon:hover {
                transform: scale(1.05);
                background-color: #f0f8ff;
            }

            .icon p {
                margin-top: 10px;
                font-size: 14px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="#home">Home</a></li>
                <li><a href="#workout" class="active">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
            </ul>
        </nav>

        <div class="icon-container">
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Walking">
                <p>Walking</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Lifting">
                <p>Lifting</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="HIIT">
                <p>HIIT</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Running">
                <p>Running</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Yoga">
                <p>Yoga</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Sports">
                <p>Sports</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Swimming">
                <p>Swimming</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Recommendation">
                <p>Recommendation</p>
            </div>
            <div class="icon">
                <img src="https://via.placeholder.com/50" alt="Cycling">
                <p>Cycling</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

# Profile Page Route
@app.route("/profile")
def profile():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Profile Page</title>
        <style>
            /* General Styles */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }

            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            nav li a:hover {
                background-color: lightblue;
                color: black;
            }

            .active {
                background-color: lightskyblue;
                color: black;
            }

            .container {
                text-align: center;
                padding: 50px 20px;
            }

            .profile-icon {
                font-size: 80px;
                border: 2px solid #000;
                border-radius: 50%;
                display: inline-block;
                width: 100px;
                height: 100px;
                line-height: 100px;
                text-align: center;
                margin-bottom: 20px;
                color: #000;
            }

            .profile-details {
                border: 1px solid #333;
                padding: 20px;
                display: inline-block;
                text-align: left;
                background-color: #fff;
                margin-bottom: 20px;
            }

            .buttons {
                margin-top: 20px;
            }

            .buttons button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin: 0 10px;
            }

            .buttons button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/">Home</a></li>
                <li><a href="#workout">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
                <li style="float:right"><a class="active" href="/">Account</a></li>
            </ul>
        </nav>

        <div class="container">
            <div class="profile-icon">
                <span>&#128100;</span> <!-- Unicode for user icon -->
            </div>
            <div class="profile-details">
                <p><strong>Name:</strong> [Your Name]</p>
                <p><strong>Address:</strong> [Your Address]</p>
                <p><strong>Phone Number:</strong> [Your Phone Number]</p>
                <p><strong>Biography:</strong> [Short Bio]</p>
            </div>
            <div class="buttons">
                <button>Edit Profile</button>
                <button>Logout</button>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)

