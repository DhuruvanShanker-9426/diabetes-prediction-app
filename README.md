# 🩺 Diabetes Prediction App

## 📌 Overview

This project is a **Machine Learning web application** that predicts whether a person is likely to have diabetes based on medical inputs.
It uses **Logistic Regression** and is deployed using **Streamlit** for an interactive user experience.

---

## 🎯 Problem Statement

Early detection of diabetes is crucial for effective treatment.
This application helps estimate diabetes risk based on patient health metrics.

---

## 📊 Features Used

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin Level
* BMI (Body Mass Index)
* Diabetes Pedigree Function (Family History Score)
* Age

---

## ⚙️ Model Details

* Algorithm: Logistic Regression
* Output: Probability (0–1)
* Threshold: 0.3 (to prioritize recall)

---

## 🚀 App Features

* Clean 2-column user interface
* Real-time prediction
* Probability display with progress bar
* Risk classification (Low / Medium / High)
* Precision & Recall explanation
* Input summary display

---

## 🧠 Model Insight

* **Recall** is prioritized to avoid missing diabetes cases
* **Precision** ensures prediction reliability
* Designed for healthcare-style decision support

---

## 📁 Project Structure

```
diabetes-prediction-app/
│
├── app.py
├── model/
│   └── model.pkl
├── notebooks/
│   └── model_training.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app using **Streamlit Cloud**.

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and not a medical diagnosis.

---

## 👤 Author

Dhuruvan Shanker R