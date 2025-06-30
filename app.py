import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
@st.cache_data

def load_data():
    df = pd.read_csv("EA.csv")
    return df

df = load_data()
st.set_page_config(layout="wide")
st.title("Employee Attrition Dashboard")
st.markdown("""
This interactive dashboard provides macro and micro-level insights on employee attrition trends.
Filter, visualize, and explore metrics to inform HR decision-making.
""")

# Sidebar Filters
st.sidebar.header("Filter the Data")
departments = st.sidebar.multiselect("Select Departments", options=df['Department'].unique(), default=df['Department'].unique())
job_roles = st.sidebar.multiselect("Select Job Roles", options=df['JobRole'].unique(), default=df['JobRole'].unique())
genders = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
overtime = st.sidebar.multiselect("OverTime", options=df['OverTime'].unique(), default=df['OverTime'].unique())

filtered_df = df[
    (df['Department'].isin(departments)) &
    (df['JobRole'].isin(job_roles)) &
    (df['Gender'].isin(genders)) &
    (df['OverTime'].isin(overtime))
]

st.markdown("### 📊 Overall Attrition")
st.write("Shows overall distribution of employee attrition.")
fig1 = px.pie(filtered_df, names='Attrition', title='Attrition Distribution')
st.plotly_chart(fig1)

# Tab View
with st.expander("Macro-Level Visualizations"):
    st.subheader("Attrition Count by Department")
    st.write("This chart highlights attrition across departments.")
    fig2 = px.histogram(filtered_df, x='Department', color='Attrition', barmode='group')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Attrition by Gender")
    fig3 = px.histogram(filtered_df, x='Gender', color='Attrition', barmode='group')
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Attrition by Job Role")
    fig4 = px.histogram(filtered_df, x='JobRole', color='Attrition', barmode='group')
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Attrition by Marital Status")
    fig5 = px.histogram(filtered_df, x='MaritalStatus', color='Attrition', barmode='group')
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Attrition by Business Travel")
    fig6 = px.histogram(filtered_df, x='BusinessTravel', color='Attrition', barmode='group')
    st.plotly_chart(fig6, use_container_width=True)

with st.expander("Numeric Attribute Distributions"):
    st.subheader("Age Distribution")
    fig7 = px.histogram(filtered_df, x='Age', color='Attrition')
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("Monthly Income by Attrition")
    fig8 = px.box(filtered_df, x='Attrition', y='MonthlyIncome', color='Attrition')
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("Distance From Home")
    fig9 = px.violin(filtered_df, y='DistanceFromHome', x='Attrition', box=True, color='Attrition')
    st.plotly_chart(fig9, use_container_width=True)

    st.subheader("Years At Company")
    fig10 = px.histogram(filtered_df, x='YearsAtCompany', color='Attrition')
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader("Total Working Years")
    fig11 = px.histogram(filtered_df, x='TotalWorkingYears', color='Attrition')
    st.plotly_chart(fig11, use_container_width=True)

with st.expander("Performance and Satisfaction"):
    st.subheader("Job Satisfaction")
    fig12 = px.histogram(filtered_df, x='JobSatisfaction', color='Attrition')
    st.plotly_chart(fig12, use_container_width=True)

    st.subheader("Environment Satisfaction")
    fig13 = px.histogram(filtered_df, x='EnvironmentSatisfaction', color='Attrition')
    st.plotly_chart(fig13, use_container_width=True)

    st.subheader("Work Life Balance")
    fig14 = px.histogram(filtered_df, x='WorkLifeBalance', color='Attrition')
    st.plotly_chart(fig14, use_container_width=True)

    st.subheader("Performance Rating")
    fig15 = px.histogram(filtered_df, x='PerformanceRating', color='Attrition')
    st.plotly_chart(fig15, use_container_width=True)

with st.expander("Correlations & Heatmap"):
    st.subheader("Correlation Heatmap")
    st.write("Shows correlation between numeric features.")
    corr_df = filtered_df.select_dtypes(include='number')
    fig16, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_df.corr(), annot=False, cmap="coolwarm")
    st.pyplot(fig16)

with st.expander("Data Table & Download"):
    st.subheader("Filtered Data Table")
    st.dataframe(filtered_df.head(100))
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Filtered Data", csv, "filtered_attrition.csv", "text/csv")
