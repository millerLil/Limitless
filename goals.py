from flask import Blueprint, request, redirect, url_for
import sqlite3
import database
import userStore
from jinja2 import Template

global insert_html
insert_html = ""

goals_bp = Blueprint("goals", __name__)

def get_goals(userName):
    global insert_html
    insert_html=""
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    # First pull all existing goals
    try:
        res = cur.execute("SELECT goal FROM goals WHERE userName = ?", (userName,))
        result = res.fetchall()
        print_goals(result, userName)
    except:
        print("No existing goals found.")
        result = None
        cur.close()
        conn.close()
        return False
    
    cur.close()
    conn.close()
    return True

def print_goals(result, userName):
    goalNum = 0
    for goal in result:
        goalNum=goalNum+1
        global insert_html
        insert_html= insert_html + '<li>' + goal[0] + '</li>\n'
    return True

def add_goal(userName, goal):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO goals (userName, goal) VALUES (?, ?)",
                    (userName, goal)
                    )
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = e.args[0]
        cur.close()
        conn.close()
        return message
        
    conn.commit()
    cur.close()
    conn.close()    
    print("Successful add")

    return "Successful"

def del_goal():
    return redirect(url_for("delgoal.delgoal")) 

@goals_bp.route("/", methods=('GET', 'POST'))
def goals():
    userName = userStore.get_user()
    # if this doesn't work, something is wrong with login
    get_goals(userName)
    if request.method == "POST":          
        goal = request.form["add_goal"]
        result = add_goal(userName, goal)
        if (result == "Successful"):
            print(result)
            message = result
            get_goals(userName)
        else:
            print(result)
            message = result

    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Goals</title>
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
                <li><a href="/home">Home</a></li>
                <li><a href="/workout">Workout</a></li>
                <li><a href="/about">About Us</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
                <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>
        
        <h1>Add a personal goal:</h1>
        <form method="POST">
            <input type="text" name="add_goal" placeholder="Enter your goal" required>
            <button type="submit">Submit</button>
        </form>
        <h2>Your Current Goals:</h2>
        <form method="POST">
            <ol id="goals">
                {{ goalsList }}
            </ol>
        </form>
        <br>
        <hr>
        <br>
        <form action="/delete">
            <input type="submit" value="Delete a Goal">
        </form>
        </body>
    </html>
    """)
    return template.render(goalsList=insert_html)
