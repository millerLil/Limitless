from flask import Blueprint, request, redirect, url_for

rec_bp = Blueprint("rec", __name__)

@rec_bp.route('/', methods=['GET', 'POST'])
def rec():
    workouts = [
        {'name': 'Walking', 'icon': '🚶'},
        {'name': 'Swimming', 'icon': '🏊'},
        {'name': 'Cycling', 'icon': '🚴'},
    ]
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Workout Recommendation</title>
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

            .content {
                padding: 20px;
                text-align: center;
            }

            .workout-options {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 20px;
            }

            .workout-option {
                text-align: center;
            }

            .workout-option div {
                font-size: 40px;
            }

            .footer-link {
                color: blue;
                text-decoration: underline;
                margin-top: 20px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home">Home</a></li>
                <li><a href="/workout">Workout</a></li>
                <li><a href="/goals">Goals</a></li>
                <li><a href="/about">About Us</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
            </ul>
        </nav>

        <div class="content">
            <h2>Recommendation</h2>
            <p>Based on your past activity, these are the workouts we have chosen for you:</p>
            <div class="workout-options">
                {% for workout in workouts %}
                <div class="workout-option">
                    <div>{{ workout.icon }}</div>
                    <p><strong>{{ workout.name }}</strong></p>
                </div>
                {% endfor %}
            </div>
            <a href="#" class="footer-link">Select one to track!</a>
        </div>
    </body>
    </html>
    """
    return html

