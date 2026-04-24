import streamlit as st
import joblib
import time

model=joblib.load("lr-diabetes-prediction-streamlit/model/model.pkl")

st.title("Diabetes Prediction Site")

st.info("Enter patient details to predict diabetes risk")

col1,col2=st.columns(2)

with col1:
    st.subheader("Patient Measurements")
    pregnancies=st.number_input(
        "Number of Pregnancies",
        min_value=0,
        max_value=17,
        step=1,
        value=3
    )

    glucose=st.number_input(
        "Glucose Level (mg/dL)",
        min_value=44,
        max_value=199,
        step=1,
        value=117,
        help="Normal range: 70–140 mg/dL"
    )

    blood_pressure=st.number_input(
        "Blood Pressure (Diastolic mmHg)",
        min_value=24,
        max_value=122,
        step=1,
        value=72,
        help="Normal diastolic: 60–80 mmHg"
    )

    skin_thickness=st.number_input(
        "Skin Thickness (mm)",
        min_value=7,
        max_value=99,
        step=1,
        value=28
    )

with col2:
    st.subheader("Health Indicators")
    insulin=st.number_input(
        "Insulin Level (μU/mL)",
        min_value=14,
        max_value=846,
        step=1,
        value=103,
        help="Typical fasting range varies (approx. 16–166 μU/mL)"
    )

    bmi=st.number_input(
        "Body Mass Index (BMI)",
        min_value=18.2,
        max_value=67.1,
        step=0.1,
        value=32.1,
        help="18.5–24.9 is considered normal"
    )

    diabetes_pedigree_function=st.number_input(
        "Family History Score (DPF)",
        min_value=0.08,
        max_value=2.42,
        step=0.01,
        value=0.37
    )

    age=st.number_input(
        "Age (years)",
        min_value=21,
        max_value=81,
        step=1,
        value=29
    )
st.markdown("---")

if st.button("Predict"):
    with st.spinner("Model is predicting..... please wait!!"):
        time.sleep(3)
        features=[
                    [
                        pregnancies,glucose,blood_pressure,skin_thickness,
                        insulin,bmi,diabetes_pedigree_function,age
                    ]
                ]
        
        predicted_prob=model.predict_proba(features)[0][1]
        
        threshold=0.3
        prediction= 1 if predicted_prob>=threshold else 0
        
        class_names=["No Diabetes","Diabetes"]
        result=class_names[prediction]
        
        if predicted_prob < 0.3:
            risk = "Low Risk"
        elif predicted_prob < 0.7:
            risk = "Medium Risk"
        else:
            risk = "High Risk"
        
        st.markdown("## 📊 Results") 
        st.subheader("Prediction Result")
        if prediction == 1:
            st.error(f"🔴 {result}")
        else:
            st.success(f"🟢 {result}")
            
        if risk == "Low Risk":
            st.success(f"🟢 Risk Level: {risk}")
        elif risk == "Medium Risk":
            st.warning(f"🟡 Risk Level: {risk}")
        else:
            st.error(f"🔴 Risk Level: {risk}")
        
        st.metric("Diabetes Probability", f"{predicted_prob*100:.2f}%")
        st.progress(predicted_prob)

        st.markdown("---")
        
        st.subheader("Model Insight")
        st.info("""
            📊 **Model Behavior**
            - Recall: Detects most diabetes cases (important for healthcare)
            - Precision: Ensures predictions are accurate
                """)
        
        if prediction == 1:
            st.warning("⚠️ This model prioritizes identifying diabetes cases (high recall), so some false alarms are possible.")
        else:
            st.info("✅ The model predicts no diabetes, but regular health checkups are still recommended.")

        st.markdown("---")
        
        st.subheader("Input Summary")

        st.markdown(f"""
            - **Pregnancies:** {pregnancies}  
            - **Glucose:** {glucose}  
            - **Blood Pressure:** {blood_pressure}  
            - **Skin Thickness:** {skin_thickness}  
            - **Insulin:** {insulin}  
            - **BMI:** {bmi}  
            - **DPF:** {diabetes_pedigree_function}  
            - **Age:** {age}  
            """)
        
        st.markdown("---")
st.caption("⚠️ This tool is for educational purposes only and not a medical diagnosis.")