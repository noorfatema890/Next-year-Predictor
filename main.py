from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Next Year Predictor</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: #333;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 2.5rem;
            color: #222;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            display: inline-block;
            min-width: 300px;
        }
        input {
            padding: 10px;
            font-size: 1rem;
            border-radius: 8px;
            border: 2px solid #ff6f91;
            outline: none;
            text-align: center;
            width: 120px;
        }
        button {
            padding: 10px 20px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            background: #ff6f91;
            color: white;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: #ff4f7b;
        }
        .loader {
            display: none;
            margin-top: 20px;
        }
        .spinner {
            margin: auto;
            width: 50px;
            height: 50px;
            border: 6px solid #eee;
            border-top: 6px solid #ff6f91;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .funny-text {
            margin-top: 15px;
            font-size: 1.2rem;
        }
        .result {
            margin-top: 25px;
            font-size: 1.5rem;
            background: #ffe0e9;
            padding: 15px;
            border-radius: 12px;
        }
    </style>
</head>
<body>
    <h1>Next Year Predictor</h1>
    <p>Wanna know what year comes after your year? Let’s ask my crystal ball 🔮</p>
    
    <div class="container">
        <form method="POST" action="/predict" onsubmit="showLoader()">
            <label>Enter your current year:</label><br><br>
            <input type="number" name="year" required placeholder="e.g. 2025"><br><br>
            <button type="submit">🔮 Predict My Future!</button>
        </form>
        
        <div class="loader" id="loader">
            <div class="spinner"></div>
            <div class="funny-text" id="loaderText">📖 Reading your code…</div>
        </div>
        {% if result %}
        <div class="result">{{ result }}</div>
        {% endif %}
    </div>
    
    <script>
        function showLoader() {
            document.getElementById("loader").style.display = "block";

            // Get loader text element
            const loaderText = document.getElementById("loaderText");

            // Change messages at different times
            setTimeout(() => loaderText.textContent = "⏳ Sabr rkho…", 1000); // after 1s
            setTimeout(() => loaderText.textContent = "⌛ Bs 1 second aur!", 2000); // after 2s
        }
    </script>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_PAGE)

@app.route("/predict", methods=["POST"])
def predict():
    current_year = int(request.form["year"])
    
    # Simulate 3-second "thinking"
    time.sleep(3)
    
    next_year = current_year + 1
    
    funny_responses = [
        f"The next year will be {next_year}!",
        f"After {current_year}, comes... {next_year}!",
        f"My super AI brain says the next year is {next_year}!",
        f"Next year is definitely {next_year}!"
    ]
    
    import random
    result = random.choice(funny_responses)
    
    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
