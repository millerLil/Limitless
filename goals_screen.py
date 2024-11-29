from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database for goals
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def goals_screen():
    goals = Goal.query.all()
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Goals Page</title>
        <style>
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            li {
                float: left;
            }

            li h2 {
                color: blue;
                display: block;
                color: lightblue;
                text-align: center;
                padding-left: 10px;
                text-decoration: none;
            }

            li a {
                display: block;
                color: white;
                text-align: center;
                padding-top: 27px;
                padding-left: 30px;
                text-decoration: none;
            }

            li a:hover {
                color: lightblue;
            }

            .active {
                color: white;
                padding-right: 14px;
                border-radius: 12px;
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
                border: 1px solid lightblue;
                border-radius: 5px;
                text-align: left;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .delete-button {
                background-color: #FF0000;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
                cursor: pointer;
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
                <li><a href="/workout/">Workout</a></li>
                <li><a class="active" href="/goals/">Goals</a></li>
                <li style="float:right"><a href="/account/">Account</a></li>
            </ul>
        </nav>

        <div class="container">
            <h1 style="color: lightblue;">Enter your personal goals:</h1>
            <form class="goal-form" action="/submit-goal" method="POST">
                <input type="text" name="goal" placeholder="Enter your goal" required>
                <button type="submit">Submit</button>
            </form>
            <h2>Your Goals:</h2>
            <ul class="goals-list">
                {% for goal in goals %}
                    <li>
                        {{ goal.content }}
                        <form action="/delete-goal/{{ goal.id }}" method="POST" style="display: inline;">
                            <button class="delete-button" type="submit">Delete</button>
                        </form>
                    </li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, goals=goals)

@app.route('/submit-goal', methods=['POST'])
def submit_goal():
    goal_content = request.form.get('goal')
    if goal_content:
        new_goal = Goal(content=goal_content)
        db.session.add(new_goal)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete-goal/<int:goal_id>', methods=['POST'])
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        db.session.delete(goal)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
