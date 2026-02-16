# 🎓 Student Performance Predictor

A machine learning web application that predicts student academic performance using behavioral and academic features. Built with Random Forest Regressor and deployed with Streamlit.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project predicts a student's final grade (G3) based on various academic and behavioral factors. The machine learning model analyzes patterns in student data to provide accurate performance predictions, helping educators identify students who may need additional support.

### Key Prediction Features

- **G1** - First period grade
- **G2** - Second period grade
- **Study Time** - Weekly study hours
- **Absences** - Number of school absences
- **Failures** - Past class failures
- **Age** - Student's age

---

## ✨ Features

- 🤖 **Machine Learning Model**: Random Forest Regressor with ~79% accuracy
- 🌐 **Interactive Web Interface**: User-friendly Streamlit application
- 📊 **Real-time Predictions**: Instant grade predictions based on input features
- 📈 **Data Visualization**: Performance metrics and insights
- 💾 **Model Persistence**: Pre-trained model saved with Joblib

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Algorithm** | Random Forest Regressor |
| **R² Score** | ~0.79 |
| **Library** | scikit-learn |
| **Training Method** | Train/Test Split with Feature Selection |

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** - Programming language
- **scikit-learn** - Machine learning library
- **Streamlit** - Web application framework

### Data & Model Management
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Joblib** - Model serialization

### Version Control
- **Git & GitHub** - Source code management

---

## 📂 Project Structure

```
student-performance-predictor/
│
├── app/
│   └── app.py                 # Streamlit web application
│
├── src/
│   └── train.py              # Model training script
│
├── models/
│   └── student_model.pkl     # Trained model file
│
├── data/                      # Dataset directory (not included)
│
├── requirements.txt          # Project dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vaishaliks24/Student-Performance-Predictor.git
   cd Student-Performance-Predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Running the Web Application

```bash
streamlit run app/app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Training the Model

```bash
python src/train.py
```

This will:
1. Load and preprocess the dataset
2. Train the Random Forest model
3. Evaluate model performance
4. Save the trained model to `models/student_model.pkl`

---

## 🔍 How It Works

### 1. Data Preprocessing
- Load student performance dataset
- Handle missing values
- Select relevant features
- Normalize data if needed

### 2. Model Training
```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

### 3. Model Evaluation
- Split data into training and testing sets
- Calculate R² score and other metrics
- Validate model performance

### 4. Deployment
- Save trained model using Joblib
- Load model in Streamlit app
- Accept user input and return predictions

---

## 📈 Future Enhancements

- [ ] Add more features (parental education, family support, etc.)
- [ ] Implement additional ML algorithms for comparison
- [ ] Add data visualization dashboard
- [ ] Deploy to cloud platform (Heroku/Streamlit Cloud)
- [ ] Include explainability features (SHAP values)
- [ ] Add historical performance tracking

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Vaishali KS**

- GitHub: [@Vaishaliks24](https://github.com/Vaishaliks24)

---

## 🙏 Acknowledgments

- Dataset: [Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/student+performance)
- scikit-learn Documentation
- Streamlit Community

---

## 📞 Contact

For questions or feedback, please open an issue or reach out through GitHub.

---

<div align="center">
  Made with ❤️ by Vaishali K S
</div>
```
