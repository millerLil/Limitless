from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def main_workout_screen():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Workout Page</title>
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
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                cursor: pointer;
            }

            .icon .emoji {
                font-size: 3rem; 
            }

            .icon:hover {
                transform: scale(1.05);
                background-color: #f0f8ff;
            }

            .icon p {
                margin-top: 10px;
                font-size: 16px;
                font-weight: bold;
            }

            a {
                text-decoration: none;
                color: inherit;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/">Home</a></li>
                <li><a href="/workout/" class="active">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
                <li class="account"><a href="/">Account</a></li>
            </ul>
        </nav>


        <div class="icon-container">
            <a href="/workout/walk/" class="icon">
                <div class="emoji">🚶</div>
                <p>Walking</p>
            </a>
            <a href="/workout/running/" class="icon">
                <div class="emoji">🏃</div>
                <p>Running</p>
            </a>
            <a href="/workout/swimming/" class="icon">
                <div class="emoji">🏊</div>
                <p>Swimming</p>
            </a>
            <a href="/workout/yoga/" class="icon">
                <div class="emoji">🧘</div>
                <p>Yoga</p>
            </a>
             <a href="/workout/sports/" class="icon">
                <div class="emoji">⚽</div>
                <p>Sports</p>
            </a>
            <a href="/workout/cycling/" class="icon">
                <div class="emoji">🚴</div>
                <p>Cycling</p>
            </a>
            <a href="/workout/lifting/" class="icon">
                <div class="emoji">🏋️</div>
                <p>Lifting</p>
            </a>
            <a href="/workout/rec/" class="icon">
                <div class="emoji">💡</div>
                <p>Recommendation</p>
            </a>
            <a href="/workout/hiit/" class="icon">
                <div class="emoji">🔥</div>
                <p>HIIT</p>
            </a>
        </div>
    </body>
    </html>
    """
    return html

import sqlite3
from flask import Flask, request

@app.route('/workout/<workout>/', methods=['GET', 'POST'])
def workout_form(workout):
    if request.method == 'POST':
        distance = request.form.get('distance', '0')
        calories = request.form.get('calories', '0')
        time = request.form.get('time', '0')

        # Save to database
        conn = sqlite3.connect('workouts.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO workouts (workout_type, distance, calories, time)
            VALUES (?, ?, ?, ?)
        """, (workout, distance, calories, time))
        conn.commit()
        conn.close()

        return redirect(url_for("main_workout_screen"))

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>{workout.title()} Workout</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}

            nav ul {{
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }}

            nav li {{
                float: left;
            }}

            nav li h2 {{
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }}

            nav li a {{
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }}

            nav li a:hover {{
                background-color: lightblue;
                color: black;
            }}

            nav li a.active {{
                background-color: lightskyblue;
                color: black;
            }}

            nav li:last-child {{
                float: right;
            }}

            .container {{
                padding: 20px;
                text-align: center;
            }}

            form {{
                display: inline-block;
                text-align: left;
                background-color: #f4f4f4;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}

            label {{
                display: block;
                margin-bottom: 10px;
                font-size: 16px;
                color: #333;
            }}

            input {{
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: none;
                border-bottom: 2px solid #007BFF;
                background-color: transparent;
                font-size: 16px;
                color: #333;
                outline: none;
                transition: border-color 0.3s ease;
            }}

            input:focus {{
                border-bottom: 2px solid #0056b3;
            }}

            .buttons {{
                margin-top: 20px;
                display: flex;
                gap: 10px;
                justify-content: center;
            }}

            button {{
                background-color: #007BFF;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            }}

            button:hover {{
                background-color: #0056b3;
            }}

            a button {{
                background-color: #ccc;
            }}
        </style>

    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/">Home</a></li>
                <li><a href="/workout/" class="active">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
                <li><a href="/">Account</a></li>
            </ul>
        </nav>

        <div class="container">
            <h1>{workout.title()} Workout</h1>
            <form method="POST">
                <label for="distance">Distance (miles):</label>
                <input type="text" id="distance" name="distance" placeholder="Enter distance...">
                <label for="calories">Calories Burned:</label>
                <input type="text" id="calories" name="calories" placeholder="Enter calories...">
                <label for="time">Time (minutes):</label>
                <input type="text" id="time" name="time" placeholder="Enter time...">
                <div class="buttons">
                    <button type="submit">Submit</button>
                    <a href="/"><button type="button">Back to Workout Page</button></a>
                </div>
            </form>

        </div>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(debug=True)

