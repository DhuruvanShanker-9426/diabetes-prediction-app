# 🩺 Diabetes Prediction App (ML + Streamlit)

## 📌 Overview

This project is a **Machine Learning-based web application** that predicts whether a person is likely to have diabetes based on medical attributes.
The app is built using **Logistic Regression** and deployed with **Streamlit** to provide an interactive user interface.

---

## 🎯 Problem Statement

Early detection of diabetes is important for timely medical intervention.
This project aims to assist in predicting diabetes risk using patient health data.

---

## 📊 Features Used

The model uses the following input features:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin Level
* Body Mass Index (BMI)
* Diabetes Pedigree Function (Family History Score)
* Age

---

## ⚙️ Model Details

* Algorithm: Logistic Regression
* Output: Probability of Diabetes (0 to 1)
* Threshold Used: 0.3 (to improve recall)

---

## 🚀 App Features

* User-friendly input interface
* Two-column clean UI layout
* Real-time prediction
* Probability display with progress bar
* Risk categorization (Low / Medium / High)
* Model explanation (Precision & Recall)
* Input summary display

---

## 🧠 Model Insights

* **Recall** is prioritized to ensure most diabetes cases are detected
* **Precision** ensures predictions are reasonably accurate
* Suitable for healthcare scenarios where missing a case is costly

---

## 📁 Project Structure

```
diabetes-prediction-app/
│
├── app.py
├── model/
│   └── model.pkl
├── data/
│   └── diabetes.csv
├── notebooks/
│   └── diabetes_logestic_regression.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the App

1. Clone the repository:

```
git clone https://github.com/your-username/diabetes-prediction-app.git
```

2. Navigate to the project folder:

```
cd diabetes-prediction-app
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the Streamlit app:

```
streamlit run app.py
```

---

## 🌐 Deployment

The app can be deployed using **Streamlit Cloud** or any cloud platform.

---

## ⚠️ Disclaimer

This application is for **educational purposes only** and should not be used as a medical diagnosis. Always consult a healthcare professional.

---

## 📌 Author

Dhuruvan Shanker R