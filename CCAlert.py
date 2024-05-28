import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CCAlert: Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

st.title('CCAlert: Customer Churn Prediction System')

with st.sidebar:
    st.write('\n')
    st.markdown("""
    <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff;">
    💡 Leverage AI to predict customer churn, improve retention strategies, and boost your business performance.  
    📈 Let's utilize data to make informed decisions and drive growth.
    </div>
    """, unsafe_allow_html=True)

st.header('Preventing Customer Churn', divider='rainbow')

st.write("""
Customer churn is a significant challenge for businesses, leading to lost revenue and increased costs.  
Our AI-driven system accurately predicts customer churn, allowing you to take proactive measures to retain valuable customers.
""")

st.header('How it Works', divider='rainbow')

st.write("""
Our model is trained on real-world customer data, enabling it to:

- Identify customers at high risk of churning ⚠️
- Target interventions and resources to retain customers ♻️

This AI-enabled solution can:

- Enhance customer satisfaction and loyalty 
- Decrease customer acquisition costs
- Improve overall business performance 
""")

st.header('Who Can Benefit', divider='rainbow')

st.write("""
- Subscription-based businesses
- Telecom companies
- Financial services
- Retail and e-commerce businesses
- Customer relationship management teams
""")


st.header('Contact Us', divider='rainbow')

st.markdown("""
To learn more about **CCAlert** and how it can help your organization, please reach out:

<div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff; width: fit-content;">
📧 <a href="mailto:kalpesh2003patel@gmail.com" style="text-decoration: none; color: #ffffff;">kalpesh2003patel@gmail.com</a>
</div>
""", unsafe_allow_html=True)