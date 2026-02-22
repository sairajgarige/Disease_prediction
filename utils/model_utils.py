import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def load_model(model_path='model.pkl'):
    """
    Load the trained model from a pickle file.
    """
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file {model_path} not found. Please run train_model.py first.")

def predict_disease(model, encoders, symptoms):
    """
    Predict the disease based on selected symptoms.
    symptoms: list of selected symptom names
    Returns: predicted_disease, probability, top_3_diseases
    """
    if len(symptoms) < 3:
        raise ValueError("At least 3 symptoms are required for prediction.")
    
    # Prepare input data: assume first 3 symptoms for symptom1, symptom2, symptom3
    # If more, ignore extras; if less, error already raised
    input_data = {}
    symptom_cols = ['symptom1', 'symptom2', 'symptom3', 'symptom4']
    for i, col in enumerate(symptom_cols):
        if i < len(symptoms):
            try:
                input_data[col] = encoders['symptoms'].transform([symptoms[i]])[0]
            except ValueError:
                # If symptom not seen during training, use 'None'
                input_data[col] = encoders['symptoms'].transform(['None'])[0]
        else:
            # For missing symptoms, use 'None'
            input_data[col] = encoders['symptoms'].transform(['None'])[0]
    
    # Create input array
    import pandas as pd
    input_df = pd.DataFrame([input_data])
    
    # Predict
    prediction = model.predict(input_df)[0]
    predicted_disease = encoders['disease'].inverse_transform([prediction])[0]
    
    # Probabilities
    proba = model.predict_proba(input_df)[0]
    probability = proba[prediction] * 100  # Percentage
    
    # Top 3 diseases
    top_indices = np.argsort(proba)[::-1][:3]
    top_3 = [(encoders['disease'].inverse_transform([idx])[0], proba[idx] * 100) for idx in top_indices]
    
    return predicted_disease, probability, top_3