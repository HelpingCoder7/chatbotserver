from flask import Flask, request, jsonify
from gemini import chat_with_gemini

app = Flask(__name__)

@app.route('/chatwithbot', methods=['POST'])
def chat_with_bot():
    data = request.get_json()  # Get JSON data from the request
    if not data or 'prompts' not in data:
        return jsonify({'error': 'No prompts provided or invalid format'}), 400
    
    prompts = data['prompts']  # Extract the prompts from the JSON data
    
    responses = []  # Initialize a list to store responses
    
    for prompt_part in prompts:
        gemini_response = chat_with_gemini(prompt_part)
        responses.append(gemini_response)
    
    return jsonify({'responses': responses})  # Return responses as JSON array

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
