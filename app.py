from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Global dictionary to store the latest weather data
latest_data = {"temperature": None, "humidity": None, "timestamp": None}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def receive_weather_data():
    # Receive weather data from the Arduino
    data = request.get_json()
    latest_data["temperature"] = data.get("temperature")
    latest_data["humidity"] = data.get("humidity")
    latest_data["timestamp"] = datetime.now().strftime("%H:%M:%S")

    # Log received data for debugging
    print(f"Received Temperature: {latest_data['temperature']}°C, Humidity: {latest_data['humidity']}%")

    return jsonify({"status": "success", "message": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_weather_data():
    # Provide the latest data as JSON
    return jsonify(latest_data)

if __name__ == '__main__':
    # Use the PORT environment variable if it exists; otherwise, default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
