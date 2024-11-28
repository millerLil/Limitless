from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# fake profile for now 
profile_data = {
    "name": "John Smith",
    "address": "Enter address here",
    "phone_number": "123-456-7890",
    "biography": "Enter biography here"
}

@app.route('/')
def profile():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Profile Page</title>
        <style>
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
                background-color: #ddd;
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
                <p><strong>Name:</strong> {{ profile.name }}</p>
                <p><strong>Address:</strong> {{ profile.address }}</p>
                <p><strong>Phone Number:</strong> {{ profile.phone_number }}</p>
                <p><strong>Biography:</strong> {{ profile.biography }}</p>
            </div>
            <div class="buttons">
                <form action="/edit-profile" method="GET" style="display: inline;">
                    <button>Edit Profile</button>
                </form>
                <form action="/logout" method="POST" style="display: inline;">
                    <button>Logout</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, profile=profile_data)

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
       
        profile_data["name"] = request.form.get("name")
        profile_data["address"] = request.form.get("address")
        profile_data["phone_number"] = request.form.get("phone_number")
        profile_data["biography"] = request.form.get("biography")
        return redirect(url_for('profile'))

    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Profile</title>
        <style>
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

            .edit-form-container {
                border: 1px solid #333;
                padding: 20px;
                display: inline-block;
                text-align: left;
                background-color: #fff;
                margin-bottom: 20px;
                width: 50%;
            }

            .edit-form label, .edit-form input, .edit-form textarea {
                display: block;
                margin-bottom: 10px;
                width: 100%;
            }

            .edit-form input, .edit-form textarea {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }

            button:hover {
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
            <h1>Edit Profile</h1>
            <div class="edit-form-container">
                <form class="edit-form" action="/edit-profile" method="POST">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" value="{{ profile.name }}">

                    <label for="address">Address:</label>
                    <input type="text" id="address" name="address" value="{{ profile.address }}">

                    <label for="phone_number">Phone Number:</label>
                    <input type="text" id="phone_number" name="phone_number" value="{{ profile.phone_number }}">

                    <label for="biography">Biography:</label>
                    <textarea id="biography" name="biography">{{ profile.biography }}</textarea>

                    <button type="submit">Save</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, profile=profile_data)

@app.route('/logout', methods=['POST'])
def logout():
    
    return redirect(url_for('profile'))

if __name__ == "__main__":
    app.run(debug=True)

