from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from utils.preprocessing import load_dataset, encode_data, save_encoders

def train_model():
    """
    Train the RandomForestClassifier model and save it along with encoders.
    """
    # Load dataset
    df = load_dataset()
    
    # Encode data
    df_encoded, encoders = encode_data(df)
    
    # Prepare features and target
    X = df_encoded.drop('disease', axis=1)
    y = df_encoded['disease']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Save encoders
    save_encoders(encoders)
    
    print("Model and encoders saved successfully.")

if __name__ == "__main__":
    train_model()