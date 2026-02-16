# Student-Performance-Predictor"# Student-Performance-Predictor" 
# 🎓 Student Performance Predictor

A machine learning application that predicts student final grades (G3) based on various academic and demographic factors using Random Forest Regression. Built with Streamlit for an interactive web interface.

## 📋 Overview

This project uses machine learning to predict student performance based on factors such as:
- Age
- Study time
- Absences
- Previous grades (G1 and G2)
- Past failures

The model is trained using a Random Forest Regressor with hyperparameter tuning via GridSearchCV to achieve optimal performance.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **ML Model**: Random Forest Regressor with optimized hyperparameters
- **Feature Importance Visualization**: Display which features most impact predictions
- **Real-time Predictions**: Get instant grade predictions based on input parameters

## 🏗️ Project Structure

```
Student-Performance-Predictor/
├── app/
│   └── app.py              # Streamlit web application
├── src/
│   └── train.py            # Model training script
├── data/
│   └── student_data.csv    # Dataset for training
├── models/
│   └── student_model.pkl   # Trained model
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md
```

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **matplotlib**: Data visualization
- **joblib**: Model serialization

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Vaishaliks24/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Training the Model

To train the model with your own data:

```bash
python src/train.py
```

The training script will:
- Load the dataset from `data/student_data.csv`
- Perform preprocessing (scaling for numeric features)
- Train a Random Forest model with hyperparameter tuning
- Evaluate the model using R² score
- Save the trained model to `models/student_model.pkl`

### Running the Web Application

Launch the Streamlit app:

```bash
streamlit run app/app.py
```

Then open your browser to `http://localhost:8501`

### Making Predictions

1. Input the following parameters in the web interface:
   - **Age**: Student's age (15-25)
   - **G1**: First period grade (0-20)
   - **G2**: Second period grade (0-20)
   - **Study Time**: Weekly study time (1-4 scale)
   - **Absences**: Number of school absences (0-100)
   - **Past Failures**: Number of past class failures (0-3)

2. Click **Predict** to get the predicted final grade (G3)

3. View the feature importance chart to understand which factors most influence the prediction

## 📊 Model Details

- **Algorithm**: Random Forest Regressor
- **Preprocessing**: StandardScaler for numeric features
- **Hyperparameter Tuning**: GridSearchCV with 5-fold cross-validation
- **Evaluation Metric**: R² Score
- **Tuned Parameters**:
  - `n_estimators`: [100, 200]
  - `max_depth`: [None, 10, 20]

## 📁 Dataset

The model expects a CSV file with the following columns:
- `age`: Student's age
- `studytime`: Weekly study time
- `absences`: Number of absences
- `G1`: First period grade
- `G2`: Second period grade
- `G3`: Final grade (target variable)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Vaishaliks24**
- GitHub: [@Vaishaliks24](https://github.com/Vaishaliks24)

## 🙏 Acknowledgments

- Dataset inspired by student performance data
- Built with ❤️ using Streamlit and scikit-learn

---

⭐ If you find this project useful, please consider giving it a star!
