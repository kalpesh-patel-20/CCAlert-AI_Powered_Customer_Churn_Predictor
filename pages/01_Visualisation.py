import streamlit as st
import matplotlib.pyplot as plt

with st.sidebar:
    st.write('\n')
    st.markdown("""
    <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff;">
    📊 **Gain insights from visualization**  
    🔍 Explore data trends and patterns through interactive chart .
    </div>
    """, unsafe_allow_html=True)

# Data
labels = ["Churn: Yes", "Churn: No"]
values = [1869, 5163]
labels_gender = ["F", "M", "F", "M"]
sizes_gender = [939, 930, 2544, 2619]
colors = ['#ff6666', '#66b3ff']
colors_gender = ['#c2c2f0', '#ffb3e6', '#c2c2f0', '#ffb3e6']
explode = (0.3, 0.3)
explode_gender = (0.1, 0.1, 0.1, 0.1)
textprops = {"fontsize": 15, "color": "white"}

fig, ax = plt.subplots(figsize=(5, 5))

ax.pie(values, labels=labels, autopct='%1.1f%%', pctdistance=1.08, 
       labeldistance=0.8, colors=colors, startangle=90, frame=True, 
       explode=explode, radius=10, textprops=textprops, counterclock=True)


ax.pie(sizes_gender, labels=labels_gender, colors=colors_gender, 
       startangle=90, explode=explode_gender, radius=7, 
       textprops=textprops, counterclock=True)


centre_circle = plt.Circle((0, 0), 5, color='white', fc='#0E1117', linewidth=0)
ax.add_artist(centre_circle)


fig.set_facecolor("#0E1117")


ax.axis('equal')
plt.tight_layout()


col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<h2 style='text-align: left; color: white;'>Insights</h2>", unsafe_allow_html=True)
    st.markdown("""
        - **Churn Distribution**: The chart shows the distribution of churned and non-churned customers.
        - **Gender Distribution**: Inside the main chart, the gender distribution is represented, with different colors for male (M) and female (F) customers.
        - **Churn Percentage**: The outer circle shows that around 27% of the customers have churned.
        - **Non-Churn Percentage**: The remaining 73% are still with the company.
    """)
    
with col2:
    st.pyplot(fig)
