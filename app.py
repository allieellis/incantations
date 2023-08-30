from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'  # Replace with your OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.json.get('description')
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates rhyming incantations for magical spells."},
        {"role": "user", "content": f"Write a rhyming incantation for a spell that {description}."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    incantation = response.choices[0].message['content'].strip()
    return jsonify(incantation=incantation)

if __name__ == '__main__':
    app.run(debug=True)
