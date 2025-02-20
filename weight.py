from flask import Blueprint, request
import sqlite3
import userStore
import database

weight_bp = Blueprint("weight",__name__)

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    userName = userStore.get_user()
    # if this doesn't work, something is wrong with login

    if request.method == 'POST':
        # Get data from the form
        weight = float(request.form.get('weight'))
        database.update_Weight(userName,weight)
        userStore.set_weight(weight)

    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lifting Tracker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
                        
            .list {
                text-align: left;
                margin-left: 10px;
            }
                        
            form div {
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="/workout/">Workout</a>
        </nav>

        <img src="data:image/png;base64,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" alt="Person Working Out" style="width: 150px; height: 150px; margin-bottom: 20px;">

        <h2>Please enter your current weight</h2>
        <form method="POST">
            <div>
                <label for="weight">Current weight:</label>
                <input type="number" step="0.1" id="weight" name="weight" required>
            </div>
            <div style="margin-top: 20px; font-family: sans-serif">
                <button type="submit">Submit</button>
            </div>
        </form>

    </body>
    </html>
    """
    return html