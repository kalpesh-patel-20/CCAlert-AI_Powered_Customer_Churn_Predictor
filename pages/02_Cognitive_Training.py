import streamlit as st
import subprocess

with st.sidebar:
    st.write('\n')
    st.markdown("""
    <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff;">
    🚀 Model Training Process<br>  
    🛠️ Train your model here
    </div>
    """, unsafe_allow_html=True)


st.header("Customer Churn Prediction Model Training", divider="rainbow")
st.write("Initiate the model training process by clicking the 'Start' button. Please be aware that the duration of this training may vary, depending on the performance specifications of your device. Thank you for your patience.")


def start_training():
    st.write("Magic is happening......")
    with st.spinner("🧠 Training the Machine Learning model..."):
        subprocess.run(["python", "main.py"])
        st.success("Model training completed.")

if st.button("Start"):
    start_training()