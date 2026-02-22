import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import os

def load_dataset(file_path='dataset.csv'):
    """
    Load the dataset from CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file {file_path} not found.")
    df = pd.read_csv(file_path)
    return df

def get_unique_symptoms(df):
    """
    Get a list of unique symptoms from the dataset.
    """
    symptoms = []
    for col in df.columns[:-1]:  # Exclude disease column
        symptoms.extend(df[col].dropna().unique())
    return sorted(list(set(symptoms)))

def encode_data(df):
    """
    Encode the symptom columns and disease column using LabelEncoder.
    Returns encoded dataframe and the encoders.
    """
    df_encoded = df.copy()
    encoders = {}
    
    # Collect all unique symptoms
    all_symptoms = []
    for col in df.columns[:-1]:  # All columns except the last (disease)
        all_symptoms.extend(df[col].dropna().unique())
    all_symptoms = list(set(all_symptoms))
    
    # Fit one encoder for all symptoms
    symptom_encoder = LabelEncoder()
    symptom_encoder.fit(all_symptoms + ['None'])
    encoders['symptoms'] = symptom_encoder
    
    # Encode symptom columns
    for col in df.columns[:-1]:
        df_encoded[col] = symptom_encoder.transform(df[col].fillna('None'))
    
    # Encode disease column
    disease_encoder = LabelEncoder()
    df_encoded['disease'] = disease_encoder.fit_transform(df['disease'])
    encoders['disease'] = disease_encoder
    
    return df_encoded, encoders

def save_encoders(encoders, file_path='encoder.pkl'):
    """
    Save the encoders to a pickle file.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(encoders, f)

def load_encoders(file_path='encoder.pkl'):
    """
    Load the encoders from a pickle file.
    """
    with open(file_path, 'rb') as f:
        return pickle.load(f)