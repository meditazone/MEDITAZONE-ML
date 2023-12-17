from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle

app = Flask(__name__)

# Instantiate Tokenizer
vocab_size = 5000
embedding_dim = 64
max_length = 250
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"

# Path Model
model_path = "C:\\Users\\Dimas Dwi A\\Downloads\\ML\\model.h5"
model = load_model(model_path)

# Load the saved Tokenizer
tokenizer_path = "C:\\Users\\Dimas Dwi A\\Downloads\\ML\\tokenizer.pkl"
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input text from the request
        data = request.get_json(force=True)
        if 'text' in data:
            user_text = data['text']
            
            #labels = LabelEncoder()
            labels = ["Anxiety", "Depression", "Stress"]
            
            # Pre-process the input data
            sequences = tokenizer.texts_to_sequences(user_text)
            padded_data = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
            
            # Make predictions using the loaded model
            predictions = model.predict(padded_data)
                
            # Process predictions and return the results
            results = []
            result = {
                'text': user_text,
                'predictions': [
                    {'class': labels[j], 'probability': float(predictions[0][j])}
                    for j in range(len(predictions[0]))
                ],
                'predicted_class': labels[np.argmax(predictions[0])]
            }
            results.append(result)

            return jsonify(results)

        else:
            return jsonify({'error': "'text' key not found in data"})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
