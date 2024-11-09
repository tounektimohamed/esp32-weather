from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def receive_weather_data():
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    # Process the data or store it in the database
    print(f"Received Temperature: {temperature}°C, Humidity: {humidity}%")

    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # SSL context for HTTPS
