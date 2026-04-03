# Student Exam Score Predictor:

# Overview:

A Machine Learning web application that predicts student exam performance based on academic, personal, and environmental factors.
This project demonstrates how different inputs influence student success using a regression-based approach.

# Live Demo:

https://student-exam-score-predictor-exa4ez69vmuuk9e9jhg58m.streamlit.app/

# Key Features:

- Predicts student exam score using Machine Learning
- Uses 19 input features
- Interactive Streamlit web interface
- User-friendly input selection (Low / Medium / High)
- Real-time prediction output

# Model Details:

- Algorithm: Linear Regression
- Evaluation Metric: R² Score
- Achieved R² Score: 0.77

# Tech Stack:

- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit

# How It Works:

1. User selects input features
2. Data is processed and encoded
3. Model predicts exam score
4. Result is displayed instantly

# Prediction Output:

Predicts student exam score based on user inputs.

# Project Preview:
# Input Interface & Output Prediction:

<img width="1827" height="852" alt="input_data" src="https://github.com/user-attachments/assets/e312317c-81ca-4786-a026-a005c0c4085d" />
<img width="1801" height="900" alt="output_predict" src="https://github.com/user-attachments/assets/3fff8e52-20ea-422a-97de-5625bbda31cd" />

# Use Case:

- Helps students estimate their performance
- Useful for educators to analyze student factors
- Demonstrates a real-world Machine Learning application

# Project Structure:

- "app.py" – Streamlit web application
- "train.py" – Model training script
- "requirements.txt" – Project dependencies
- "README.md" – Project documentation
- "model/"
  - "model.pkl" – Trained model
- "data/"
  - "dataset.csv" – Input dataset
- "images/"
  - "input.png" – Input interface screenshot
  - "output.png" – Prediction result screenshot

# How to Run Locally:

* git clone https://github.com/kumarsrigiribharath-lab/Student-Exam-Score-predictor/tree/main
* cd Student-Exam-Score-predictor
* pip install -r requirements.txt
* python train.py
* streamlit run app.py

# Key Learnings:

- Regression modeling using Linear Regression
- Feature preprocessing and encoding
- Building interactive ML applications
- Deploying ML models using Streamlit

# Future Enhancements:

- Add data visualization dashboard
- Experiment with advanced models (Random Forest, XGBoost)
- Improve prediction accuracy
- Enhance UI/UX

# Author:

Srigiribharath K
Aspiring Machine Learning Engineer

# Support:

If you find this project useful, consider giving it a star on GitHub.
