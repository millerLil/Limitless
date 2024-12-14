from flask import Blueprint, request, redirect, url_for
import sqlite3
import database
import userStore
import getCalories
from jinja2 import Template

global insert_html
insert_html = ""
global actList
actList = []

cycle_bp = Blueprint("cycle", __name__)

def get_cycles(userName):
    global insert_html
    insert_html = ""
    conn = database.get_db_connection()
    cur = conn.cursor()
    actType = "cycling"
    try:
        res = cur.execute("SELECT * FROM activities WHERE userName = ? AND activity = ?", (userName, actType))
        result = res.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        result = None
        cur.close()
        conn.close()
        return False

    if len(result) == 0:
        insert_html = "No cycling activities found"
        return False

    print_activities(result, userName)
    cur.close()
    conn.close()
    return True

def print_activities(result, userName):
    global insert_html
    insert_html = ""
    if result == "No cycling activities found":
        insert_html = result
    else:
        for activity in result:
            insert_html += f'<li>{activity[2]}: {activity[3]} minutes, {activity[4]} calories, {activity[5]} oz of water</li>\n'
    return True

def add_activity(userName, act, miles, cal, water):
    conn = database.get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO activities (userName, activity, actNum, calories, water) VALUES (?, ?, ?, ?, ?)",
                    (userName, act, miles, cal, water))
        message = "Successful activity add"
    except sqlite3.Error as e:
        print(f"Error: {e}")
        message = e.args[0]

    conn.commit()
    cur.close()
    conn.close()
    return message


@cycle_bp.route('/', methods=['GET', 'POST'])
def cycle():
    userName = userStore.get_user()
    if not get_cycles(userName):
        print("No cycling activities found or database error.")

    if request.method == 'POST':
        minutes = request.form.get('minutes')
        intensity = request.form.get('intensity')
        water = request.form.get('water')
        calories = getCalories.get_calories("cycling", intensity, minutes)
        if calories == -1:
            print("No weight registered")
            calories = 0
        result = add_activity(userName, "cycling", minutes, calories, water)
        if result == "Successful activity add":
            get_cycles(userName)

    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cycling Tracker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                text-align: center;
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

            .list {
                text-align: left;
                margin-left: 10px;
            }

            form div {
                margin: 10px 0;
            }

            img {
                margin: 20px 0;
                width: 100px;
                height: 100px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }

            h2 {
                margin-top: 10px;
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

        <img src="/static/img/cycling.png" alt="Cycling Image">
        <h2>Cycling</h2>
        <form method="POST">
            <div class="act-container">
                <div>
                    <label for="minutes">Minutes:</label>
                    <input type="integer" id="minutes" name="minutes" required>
                </div>
                <div>
                    <label for="intensity">Intensity:</label>
                    <select name="intensity" id="intensity" required>
                        <option selected value="low">Low</option>
                        <option value="moderate">Moderate</option>
                        <option value="high">High</option>
                    </select>
                </div>
            </div>
            <div class="addl-container">
                <div>
                    <label for="water">Water (oz):</label>
                    <input type="text" id="water" name="water" required>
                </div>
            </div>
            <div style="margin-top: 20px;">
                <button type="submit">Submit</button>
            </div>
        </form>
        <hr>
        <h2>Your Current Cycling Activities:</h2>
        <ol id="cycles" class="list">
            {{ actList }}
        </ol>
        <br><hr><br>
    </body>
    </html>
    """)
    return template.render(actList=insert_html)
