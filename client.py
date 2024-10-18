from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction pour trier une partie des données
def sort_data(data):
    return sorted(data)

# API pour recevoir les données et les trier
@app.route('/sort', methods=['POST'])
def sort_endpoint():
    data = request.get_json().get('data', [])
    sorted_data = sort_data(data)
    return jsonify(sorted_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
