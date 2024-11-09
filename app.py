from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Global dictionary to store the latest weather data
latest_data = {"temperature": None, "humidity": None, "timestamp": None}

@app.route('/')
def home():
    # Confirm index.html is found
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error loading index.html: {e}")
        return "Error loading page", 500

@app.route('/weather', methods=['POST'])
def receive_weather_data():
    data = request.get_json()
    latest_data["temperature"] = data.get("temperature")
    latest_data["humidity"] = data.get("humidity")
    latest_data["timestamp"] = datetime.now().strftime("%H:%M:%S")

    print(f"Received Temperature: {latest_data['temperature']}°C, Humidity: {latest_data['humidity']}%")
    return jsonify({"status": "success", "message": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_weather_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    # Using Render's PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)
