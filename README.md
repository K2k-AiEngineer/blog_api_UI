# 🌱 Vegan and Non-Vegan Text Classification API

Welcome to the Vegan and Non-Vegan Text Classification API! This Flask application uses a pre-trained zero-shot classification model to classify text as either "vegan" or "non-vegan". The goal of this project is to assist users in determining the classification of various texts based on their content.


## 📁 Folder Structure

```bash
blog_api_UI/
├── model/                     # Directory containing the model files
│   ├── config.json            # Model configuration file
│   ├── merges.txt             # Tokenizer merges
│   ├── model.safetensors      # Model weights
│   ├── tokenizer.json          # Tokenizer configuration
│   ├── tokenizer_config.json   # Tokenizer parameters
│   └── vocab.json             # Vocabulary for the tokenizer
├── templates/                 # Folder containing HTML files
│   └── index.html             # Frontend for text classification
├── app.py                     # Main Flask application file
├── requirements.txt           # List of dependencies and libraries
└── README.md                  # Project documentation
```

## 📜 Description
The application is built using Flask, a lightweight WSGI web application framework in Python. It utilizes the Hugging Face transformers library to load a pre-trained model for zero-shot classification.

### Key Features
1. Zero-shot classification: Classifies text into predefined categories without requiring fine-tuning.
2. Web interface: Simple HTML form for users to input text and receive classification results.
3. Simulated processing time: Mimics real-world processing time based on text length for a more realistic user experience.

🚀 Installation and Setup
Prerequisites
Python 3.7+
pip for installing Python packages

Step 1: Clone the Repository
git clone <repository_url>
cd blog_api_UI


Step 2: Install Dependencies
Install the required packages listed in requirements.txt:
pip install -r requirements.txt

Step 3: Model Files
Ensure that you have the following model files in the model directory:
config.json
merges.txt
model.safetensors
tokenizer.json
tokenizer_config.json
vocab.json
These files are necessary for loading the model and tokenizer correctly.

Step 4: Run the Application
To start the Flask application, run the following command:

python app.py
You can access the application by navigating to http://localhost:5000 in your web browser.

## 🛠️ Usage
Open your web browser and go to http://localhost:5000.
Enter the text you want to classify in the input box.
Click the Classify button.
The classification result (either "vegan" or "non-vegan") and the confidence score will be displayed on the page.


## 🔧 API Endpoint
Endpoint: /classify
Method: POST
Request Body:
text: The text to be classified.
Example Request


```bash
curl -X POST -F 'text=This is a delicious vegan recipe!' http://localhost:5000/classify
```

### Example Response
```bash
{
  "classification": "vegan",
  "confidence_score": 95.5
}
```

##🔍 Explanation of Key Files
app.py: The main Flask application file that contains the backend logic. It loads the model and tokenizer, defines the API routes, and handles incoming requests.

model/: This directory contains all necessary files for the model, including configuration and tokenizer files.

templates/index.html: A simple HTML page for the frontend where users can input text for classification.

requirements.txt: Lists all Python packages required to run the application, including Flask and Hugging Face transformers.

