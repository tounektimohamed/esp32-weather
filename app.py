from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Variable globale pour stocker les dernières données reçues
latest_data = {'temperature': None, 'humidity': None}

@app.route('/')
def index():
    # Afficher la page d'accueil avec les dernières données
    return render_template('index.html', data=latest_data)

@app.route('/weather', methods=['POST'])
def weather():
    # Récupérer les données JSON envoyées depuis l'Arduino
    data = request.get_json()
    
    # Mettre à jour les données globales
    latest_data['temperature'] = data.get('temperature')
    latest_data['humidity'] = data.get('humidity')
    
    # Retourner une réponse JSON pour confirmer la réception des données
    return jsonify({'status': 'success', 'message': 'Data received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
