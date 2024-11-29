from flask import Blueprint

goals_bp = Blueprint("goals", __name__)

@goals_bp.route("/")
def goals():
    html = """
     <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Goals Page</title>
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
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }

            .goal-form {
                margin-bottom: 20px;
            }

            .goal-form input {
                padding: 10px;
                width: 70%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            .goal-form button {
                padding: 10px 20px;
                background-color: lightblue;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }

            .goal-form button:hover {
                background-color: #0056b3;
            }

            .goals-list {
                margin-top: 20px;
                list-style-type: none;
                padding: 0;
            }

            .goals-list li {
                background-color: #fff;
                margin: 10px auto;
                padding: 15px;
                width: 50%;
                text-align: left;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .goals-form-container {
                border: 2px solid lightblue;
                padding: 5px;
                width: 80%;
            }

            .goals-container {
                border: 2px solid lightblue;
                padding: 5px;
                width: 80%;
            }

            .delete-button {
                background-color: #FF0000;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
                cursor: pointer;
            }

            .form-submit {
                background-color: darkgray;
                color: white;
                border-radius: 2px;
            }

            .form-submit:hover {
                background-color: lightblue;
                color: black;
            }

            .delete-button:hover {
                background-color: #CC0000;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home/">Home</a></li>
                <li><a href="/workout/" class="active">Workout</a></li>
                <li><a href="/goals/">Goals</a></li>
                <li style="float:right"><a class="active" href="/account/">Account</a></li> 
            </ul>
        </nav>
        
        <div class="goals-form-container">
            <h1>Enter your personal goals:</h1>
            <form action="/submit-goal" method="POST">
                <input type="text" name="goal" placeholder="Enter your goal" required>
                <button class="form-submit" type="submit">Submit</button>
            </form>
        </div>

        <br></br>

        <div class="goals-container">
            <h2>Your Goals:</h2>
            <ul>
                {% for goal in goals %}
                    <li>{{ goal.strip() }}</li>
                    <button class="delete-button">X</button>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return html
