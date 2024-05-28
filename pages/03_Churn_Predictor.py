import streamlit as st
import numpy as np
from src.ChurnPredictor.pipeline.prediction import PredictionPipeline

with st.sidebar:
    st.write('\n')
    st.markdown("""
    <div style="padding: 20px; border: 2px solid #ffffff; border-radius: 10px; background-color: #0E1117; color: #ffffff;">
    🔍 Predict and prevent customer churn with our advanced AI solution.<br>
    🌟 Identify at-risk customers early and take proactive steps to retain them.<br> 
    🚀 Boost your business performance with actionable insights and data-driven strategies.
    </div>
    """, unsafe_allow_html=True)

st.header('Customer Churn Prediction', divider='rainbow')
st.write("Please enter the requested details of the customer, and the model will predict whether the customer is likely to churn or not.")

gender_dict = {'Male': 0, 'Female': 1}
partner_dict = {'No': 0, 'Yes': 1}
dependents_dict = {'No': 0, 'Yes': 1}
phone_service_dict = {'No': 0, 'Yes': 1}
multiple_lines_dict = {'No phone service': 0, 'No': 1, 'Yes': 2}
internet_service_dict = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
online_security_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
online_backup_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
device_protection_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
tech_support_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
streaming_tv_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
streaming_movies_dict = {'No': 0, 'Yes': 1, 'No internet service': 2}
contract_dict = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
paperless_billing_dict = {'No': 0, 'Yes': 1}
payment_method_dict = {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}

# Data collection form
with st.form("churn_form", border=True):

    gender = st.selectbox("Gender", options=gender_dict.keys())
    senior_citizen = st.selectbox("Senior Citizen", options=[0, 1])
    partner = st.selectbox("Partner", options=partner_dict.keys())
    dependents = st.selectbox("Dependents", options=dependents_dict.keys())
    tenure = st.number_input("Tenure", min_value=0, max_value=72)
    phone_service = st.selectbox("Phone Service", options=phone_service_dict.keys())
    multiple_lines = st.selectbox("Multiple Lines", options=multiple_lines_dict.keys())
    internet_service = st.selectbox("Internet Service", options=internet_service_dict.keys())
    online_security = st.selectbox("Online Security", options=online_security_dict.keys())
    online_backup = st.selectbox("Online Backup", options=online_backup_dict.keys())
    device_protection = st.selectbox("Device Protection", options=device_protection_dict.keys())
    tech_support = st.selectbox("Tech Support", options=tech_support_dict.keys())
    streaming_tv = st.selectbox("Streaming TV", options=streaming_tv_dict.keys())
    streaming_movies = st.selectbox("Streaming Movies", options=streaming_movies_dict.keys())
    contract = st.selectbox("Contract", options=contract_dict.keys())
    paperless_billing = st.selectbox("Paperless Billing", options=paperless_billing_dict.keys())
    payment_method = st.selectbox("Payment Method", options=payment_method_dict.keys())
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, format="%.2f")
    total_charges = st.number_input("Total Charges", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("Submit")

if submitted:
    data = [
        gender_dict[gender], int(senior_citizen), partner_dict[partner], dependents_dict[dependents], int(tenure),
        phone_service_dict[phone_service], multiple_lines_dict[multiple_lines], internet_service_dict[internet_service],
        online_security_dict[online_security], online_backup_dict[online_backup], device_protection_dict[device_protection],
        tech_support_dict[tech_support], streaming_tv_dict[streaming_tv], streaming_movies_dict[streaming_movies],
        contract_dict[contract], paperless_billing_dict[paperless_billing], payment_method_dict[payment_method],
        float(monthly_charges), float(total_charges)
    ]

    data = np.array(data).reshape(1, -1)

    obj = PredictionPipeline()
    predicted_value = obj.predict(data)

    if predicted_value == 1:
        st.error("The customer is likely to churn.", icon="🚨")
    elif predicted_value == 0:
        st.success("The customer is not likely to churn.", icon="✅")
