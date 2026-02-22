from flask import Flask, render_template, request, redirect, url_for
from utils.preprocessing import load_dataset, get_unique_symptoms
from utils.model_utils import load_model, predict_disease
from utils.db_config import get_db_connection, create_table
import traceback

app = Flask(__name__)

# Load model and encoders at startup
try:
    model = load_model()
    from utils.preprocessing import load_encoders
    encoders = load_encoders()
    symptoms_list = get_unique_symptoms(load_dataset())
except Exception as e:
    print(f"Error loading model or data: {e}")
    model = None
    encoders = None
    symptoms_list = []

# Create database table if not exists
create_table()

@app.route('/')
def home():
    """
    Home page with symptom selection form.
    """
    return render_template('index.html', symptoms=symptoms_list)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction request.
    """
    try:
        selected_symptoms = request.form.getlist('symptoms')
        if len(selected_symptoms) < 3:
            return render_template('index.html', symptoms=symptoms_list, error="Please select at least 3 symptoms.")
        
        if model is None or encoders is None:
            return render_template('index.html', symptoms=symptoms_list, error="Model not loaded. Please train the model first.")
        
        predicted_disease, probability, top_3 = predict_disease(model, encoders, selected_symptoms)
        
        # Store in database
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            symptoms_str = ', '.join(selected_symptoms)
            cursor.execute("""
                INSERT INTO predictions (symptoms, predicted_disease, probability)
                VALUES (?, ?, ?)
            """, (symptoms_str, predicted_disease, probability))
            connection.commit()
            cursor.close()
            connection.close()
        
        return render_template('result.html', 
                               selected_symptoms=selected_symptoms,
                               predicted_disease=predicted_disease,
                               probability=probability,
                               top_3=top_3)
    except Exception as e:
        print(traceback.format_exc())
        return render_template('index.html', symptoms=symptoms_list, error=f"An error occurred: {str(e)}")

@app.route('/history')
def history():
    """
    Display prediction history.
    """
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, symptoms, predicted_disease, probability, created_at FROM predictions ORDER BY created_at DESC")
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template('history.html', history=rows)
        else:
            return render_template('history.html', history=[], error="Database connection failed.")
    except Exception as e:
        print(traceback.format_exc())
        return render_template('history.html', history=[], error=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)