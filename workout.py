from flask import Blueprint, request, redirect, url_for

workout_bp = Blueprint("workout", __name__)

@workout_bp.route("/", methods=["GET", "POST"])
def workout():
    if request.method == "POST":
        # Redirect to the workout page if the Workout button is clicked
        if request.form.get("action") == "Walking":
            return redirect(url_for("walk.walk"))  
        if request.form.get("action") == "Recommendation":
            return redirect(url_for("rec.rec"))  

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
                <li><a href="/home">Home</a></li>
                <li><a href="/workout">Workout</a></li>
                <li><a href="/goals">Goals</a></li>
                <li><a href="/about">About Us</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
                <li style="float:right"><a class="active" href="/profile">Profile</a></li>

            </ul>
        </nav>

        <div class="icon-container">
            <div class="icon">
                <img src="/static/img/walking.jpg" alt="Walking">
                <p><a href='/walk/'>Walking</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/weightlifting.png" alt="Lifting">
                <p><a href='/lift/'>Lifting</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/HIIT.jpg" alt="HIIT">
                <p><a href='/hiit/'>HIIT</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/running.jpg" alt="Running">
                <p><a href='/run/'>Running</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/yoga.png" alt="Yoga">
                <p><a href='/yoga/'>Yoga</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/sports.png" alt="Sports">
                <p><a href='/sports/'>Sports</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/swim.png" alt="Swimming">
                <p><a href ='/swim/'>Swimming</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/recommendation.png" alt="Recommendation">
                <p><a href='/rec/'>Recommendation</a></p>
            </div>
            <div class="icon">
                <img src="/static/img/cycle.jpg" alt="Cycling">
                <p><a href='/cycle/'>Cycling</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return html
