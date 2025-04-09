from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load constitution data
with open('data/constitution.json') as f:
    constitution_data = json.load(f)

# Initialize OpenAI client with validation
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found in .env file\n"
        "Please create a .env file with:\n"
        "OPENAI_API_KEY=your-api-key-here"
    )
client = OpenAI(api_key=api_key)

@app.route('/')
def home():
    # Test environment variable loading
    api_key_set = os.getenv('OPENAI_API_KEY') is not None
    return render_template('index.html', api_key_set=api_key_set)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = []
    
    for part in constitution_data:
        for article in part['articles']:
            if query in article['title'].lower() or query in article['content'].lower():
                results.append({
                    'part': part['name'],
                    'article': article['title'],
                    'content': article['content']
                })
    
    return jsonify(results)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    
    # Create context from constitution
    context = "Indian Constitution Articles:\n"
    for part in constitution_data:
        for article in part['articles']:
            context += f"{article['title']}: {article['content']}\n"
    
    # Get AI response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a legal assistant specializing in the Indian Constitution. Provide accurate, concise answers based on the following:" + context},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )
    
    return jsonify({'answer': response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)
