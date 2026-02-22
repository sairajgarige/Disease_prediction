# AI-Powered Disease Prediction System

A comprehensive web application that uses machine learning to predict diseases based on user-selected symptoms. Built with Flask, scikit-learn, and SQLite for a complete end-to-end solution.

## 🚀 Features

- **Symptom-Based Disease Prediction**: Select multiple symptoms to get disease predictions
- **Machine Learning Model**: Random Forest Classifier trained on medical symptom data
- **Probability Scores**: Get prediction confidence and top 3 possible diseases
- **Web Interface**: Clean, responsive Bootstrap UI with medical theme
- **Database Integration**: SQLite database for storing prediction history
- **RESTful API**: Flask-based backend with proper error handling
- **Real-time Results**: Instant predictions with detailed results display

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask
- **Frontend**: HTML5, Bootstrap 5, CSS3
- **Machine Learning**: scikit-learn, pandas, numpy
- **Database**: SQLite
- **Model**: Random Forest Classifier with Label Encoding

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## 🔧 Installation

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd disease_prediction
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**
   ```bash
   python train_model.py
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   - Open your browser and go to: `http://localhost:5000`

## 📖 Usage

### Making Predictions

1. Navigate to the home page
2. Select at least 3 symptoms from the dropdown list
3. Click "Predict Disease"
4. View the results including:
   - Predicted disease
   - Prediction probability
   - Top 3 possible diseases with probabilities

### Viewing History

1. Click "History" in the navigation bar
2. View all previous predictions stored in the database
3. See symptoms, predicted diseases, and probabilities

## 🏗️ Project Structure

```
disease_prediction/
│
├── app.py                    # Main Flask application
├── train_model.py           # Model training script
├── dataset.csv              # Training dataset
├── requirements.txt         # Python dependencies
├── model.pkl               # Trained ML model
├── encoder.pkl             # Label encoders
│
├── templates/               # HTML templates
│   ├── index.html          # Home page with symptom form
│   ├── result.html         # Prediction results page
│   └── history.html        # Prediction history page
│
├── static/                  # Static files
│   └── style.css           # Custom CSS styles
│
└── utils/                   # Utility modules
    ├── db_config.py        # Database configuration
    ├── preprocessing.py    # Data preprocessing functions
    └── model_utils.py      # Model prediction utilities
```

## 🔌 API Endpoints

### GET /
- **Description**: Home page with symptom selection form
- **Response**: HTML page

### POST /predict
- **Description**: Process symptom selection and return prediction
- **Parameters**: symptoms (list of selected symptoms)
- **Response**: Prediction results page

### GET /history
- **Description**: Display prediction history
- **Response**: History page with database records

## 🗄️ Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptoms TEXT,
    predicted_disease TEXT,
    probability REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🤖 Model Details

### Training Data
- CSV file with symptom-disease mappings
- 4 symptom columns + 1 disease column
- 20 sample disease entries

### Model Architecture
- **Algorithm**: Random Forest Classifier
- **Encoding**: Label Encoding for categorical data
- **Features**: 4 symptom features
- **Target**: Disease prediction

### Training Process
1. Load and preprocess dataset
2. Encode symptoms and diseases
3. Train-test split (80/20)
4. Train Random Forest model
5. Save model and encoders

## 🎨 UI Features

- **Medical Theme**: Professional healthcare color scheme
- **Responsive Design**: Works on desktop and mobile
- **Glassmorphism**: Modern UI with backdrop blur effects
- **Gradient Backgrounds**: Beautiful medical-themed gradients
- **Interactive Elements**: Hover effects and smooth transitions

## 🔧 Configuration

### Database Configuration
The application uses SQLite by default. To use MySQL:

1. Install MySQL server
2. Update `utils/db_config.py` with your credentials
3. Change imports from `sqlite3` to `mysql.connector`

### Model Configuration
- Modify `train_model.py` to change model parameters
- Update dataset in `dataset.csv` for more training data
- Adjust preprocessing in `utils/preprocessing.py`

## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure `model.pkl` and `encoder.pkl` exist
   - Run `python train_model.py` to retrain

2. **Database Connection Error**
   - Check if SQLite file exists
   - Ensure write permissions in project directory

3. **Import Errors**
   - Install all requirements: `pip install -r requirements.txt`
   - Check Python version (3.10+)

4. **Prediction Errors**
   - Select at least 3 symptoms
   - Ensure symptoms are from the available list

## 📊 Sample Data

The included dataset contains sample medical data with diseases like:
- Common Cold, Flu, Heart Disease
- Food Poisoning, Migraine, Pneumonia
- And many more...

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For questions or issues:
- Check the troubleshooting section
- Review the code comments
- Ensure all dependencies are installed

---

**Built with ❤️ for healthcare innovation**
