from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
from keras.preprocessing import image
from keras.applications import InceptionV3
from keras.applications.inception_v3 import preprocess_input, decode_predictions
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load pre-trained InceptionV3 model
model = InceptionV3(weights='imagenet')

def preprocess_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def recognize_food(img_path):
    # Preprocess image
    img = preprocess_image(img_path)
    # Make predictions
    predictions = model.predict(img)
    # Decode predictions
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    # Get food label
    _, label, _ = decoded_predictions[0]
    # Get calorie information
    calorie_info = get_food_calories(label)
    return label, calorie_info

def get_food_calories(food_label):
    # Loading the dataset from CSV file
    dataset = pd.read_csv(r"C:\Users\N Sahasrith reddy\OneDrive\Desktop\food\Calorie_value1.csv")  # Update with your CSV file path
    # Search for the recognized food label in the dataset
    row = dataset.loc[dataset['food items'] == food_label.lower()]
    if not row.empty:
        calorie_value = row.iloc[0]['Calories']
        return calorie_value
    else:
        return "Calorie information not available"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize_food', methods=['POST'])
def recognize_food_endpoint():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    try:
        image_path = 'temp.jpg'  # Save image temporarily
        image_file.save(image_path)
        label, calories = recognize_food(image_path)
        return jsonify({'label': label, 'calories': calories}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

