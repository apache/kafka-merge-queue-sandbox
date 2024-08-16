from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json  # Get the JSON data from the incoming request
    # Process the data and perform actions based on the event
    print("Received webhook data:", data)
    return jsonify({'message': 'Webhook received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)
