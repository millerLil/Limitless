from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
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
                <li><a href="#home">Home</a></li>
                <li><a href="#workout" class="active">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
            </ul>
        </nav>

        <div class="icon-container">
            <a href="{{ url_for('walk') }}" class="icon">
                <div class="emoji">🚶</div>
                <p>Walking</p>
            </a>
            <div class="icon">
                <div class="emoji">🏋️</div>
                <p>Lifting</p>
            </div>
            <div class="icon">
                <div class="emoji">🔥</div>
                <p>HIIT</p>
            </div>
            <div class="icon">
                <div class="emoji">🏃</div>
                <p>Running</p>
            </div>
            <div class="icon">
                <div class="emoji">🧘</div>
                <p>Yoga</p>
            </div>
            <div class="icon">
                <div class="emoji">⚽</div>
                <p>Sports</p>
            </div>
            <div class="icon">
                <div class="emoji">🏊</div>
                <p>Swimming</p>
            </div>
            <a href="{{ url_for('rec') }}" class="icon">
                <div class="emoji">💡</div>
                <p>Recommendation</p>
            </a>
            <div class="icon">
                <div class="emoji">🚴</div>
                <p>Cycling</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)


