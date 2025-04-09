# 🍽️ Food Recognition and calorie estimator

A Flask-based web application that uses a pre-trained deep learning model (InceptionV3) to recognize food items from images and estimate their calorie content using a food dataset.

---

## 🚀 Features

- Upload an image of food and get the food item recognized
- Estimates calorie value based on a custom CSV dataset
- Uses Keras' InceptionV3 model pre-trained on ImageNet
- RESTful API endpoint for image processing
- Cross-Origin Resource Sharing (CORS) enabled for frontend integration

---

## 🧠 How It Works

1. The user uploads a food image via the web interface or API.
2. The image is processed and resized for compatibility with the InceptionV3 model.
3. The model predicts the most likely food label.
4. The label is matched with a calorie dataset to retrieve estimated calories.
5. The predicted label and calorie value are returned as JSON.

---

## 📁 Project Structure

food-recognition-app/ │ 
├── app.py # Flask app with ML model integration 
├── templates/ 
│ └── index.html # Web interface  
├── Calorie_value1.csv # CSV file with food items and calorie values 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation

---

## 🛠️ Technologies Used

- Python 3.7+
- Flask
- Flask-CORS
- TensorFlow / Keras
- InceptionV3 (pre-trained)
- Pandas
- NumPy

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/food-recognition-app.git
cd food-recognition-app
2. Create a Virtual Environment (Optional but Recommended)
bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
If requirements.txt is not present, manually install:

bash
pip install flask flask-cors tensorflow pandas numpy
4. Place the CSV File
Ensure the file Calorie_value1.csv containing food items and calorie values is placed in the correct path as expected by the code, or update the path in app.py.

🧪 Running the App
Start the development server:

bash
python app.py

The application will be available at:
http://127.0.0.1:5000

🎯 API Endpoint
POST /recognize_food
Uploads an image and returns the food label with its estimated calories.

Request
multipart/form-data

Field: image (food image file)

Response (Success: 200)
json
Copy
Edit
{
  "label": "pizza",
  "calories": 285
}
Response (Error)
json
Copy
Edit
{
  "error": "No image provided"
}
🔍 Notes
Make sure the image is a recognizable food item from the ImageNet dataset.

The calorie dataset must have matching labels (in lowercase) with ImageNet labels.

To update the model or dataset, modify get_food_calories() or retrain the model as needed.

