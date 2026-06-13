from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Beautiful Day</title>
        </head>
        <body>
            <h1>It is a beautiful day</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
