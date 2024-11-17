from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
   html = f"""
    <!DOCTYPE html>

     <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
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
        display: block;
        color: lightblue;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
      }

      li a {
          display: block;
          color: white;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
      }

    /* Change the link color to #111 (black) on hover */
      li a:hover {
          background-color: lightblue;
          color: black;
      }

      .active {
          background-color: lightskyblue;
          color: black;
      }
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
      <h2>Weekly Summary:</h2>

      <div class="cards-container">
        <h2>Achievements</h2>
        <h2>Progress</h2>
        <h2>Goals</h2>
      </div>
    </div>
  </body>
    </html>
    """
    return html

if __name__ == "__main__":
  app.run(debug=True)
