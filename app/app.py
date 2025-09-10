from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
            }
            .container {
                animation: fadeIn 2s ease-in-out;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 40px;
            }
            button {
                background: white;
                color: #764ba2;
                border: none;
                padding: 15px 30px;
                font-size: 1rem;
                border-radius: 30px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #ff9ff3;
                color: white;
                transform: scale(1.1);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome!</h1>
            <p>Project proudly created by <b>Yatesh Ingale</b></p>
            <button onclick="alert('Keep Hustling ✨🚀')">Click Me</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


