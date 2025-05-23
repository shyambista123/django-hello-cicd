from django.http import HttpResponse

def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django CI/CD Test</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #74ebd5, #acb6e5);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #333;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #2c3e50;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            .button {
                display: inline-block;
                padding: 12px 24px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                transition: background-color 0.3s;
            }
            .button:hover {
                background-color: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Django CI/CD!</h1>
            <p>Hello, world! This is a styled Django page deployed via CI/CD. Your pipeline is working perfectly!</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)