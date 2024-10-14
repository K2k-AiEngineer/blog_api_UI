from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import time

app = Flask(__name__)

# Load the model and tokenizer from the local 'model' directory
model_directory = 'model'
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForSequenceClassification.from_pretrained(model_directory)

# Create a zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_text():
    try:
        text = request.form['text']
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Simulate processing time based on the length of the input text
        time.sleep(min(len(text) / 100, 5))  # Max wait time capped at 5 seconds

        labels = ["vegan", "non-vegan"]
        result = classifier(text, candidate_labels=labels)
        classification = result['labels'][0]  # Classification result
        confidence_score = result['scores'][0] * 100  # Convert to percentage

        return jsonify({'classification': classification, 'confidence_score': confidence_score})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
