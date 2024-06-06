import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.title(":orange[_SPAN COMMUNICATIONS_]")
st.header("iVOOMi",divider = 'blue')

st.sidebar.title('File Upload')
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Read file based on extension
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Data Preparation (Convert Date to datetime)
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 

        # Create two columns for line charts
        col1, col2 = st.columns(2)

        # Plot 1: Impressions Over Time
        with col1:
            fig1 = px.line(df, x='Date', y='Impressions', title='Impressions Over Time', markers=True)
            fig1.update_traces(line_color='blue')
            fig1.update_layout(xaxis_title='Date', yaxis_title='Impressions')
            st.plotly_chart(fig1, use_container_width=True)

        # Plot 2: Clicks Over Time
        with col2:
            fig2 = px.line(df, x='Date', y='Clicks', title='Clicks Over Time', markers=True)
            fig2.update_traces(line_color='orange')
            fig2.update_layout(xaxis_title='Date', yaxis_title='Clicks')
            st.plotly_chart(fig2, use_container_width=True)

        # Create two more columns for additional line charts
        col3, col4 = st.columns(2)

        # Plot 3: Leads Over Time
        with col3:
            fig3 = px.line(df, x='Date', y='Leads', title='Leads Over Time', markers=True)
            fig3.update_traces(line_color='green')
            fig3.update_layout(xaxis_title='Date', yaxis_title='Leads')
            st.plotly_chart(fig3, use_container_width=True)

        # Plot 4: CPL Over Time
        with col4:
            fig4 = px.line(df, x='Date', y='CPL', title='CPL Over Time', markers=True)
            fig4.update_traces(line_color='purple')
            fig4.update_layout(xaxis_title='Date', yaxis_title='CPL')
            st.plotly_chart(fig4, use_container_width=True)
            
        # Plot 5: Scatter Plot of Leads vs Impressions
        fig5 = px.scatter(df, x='Impressions', y='Leads', color='Leads',
                         title='Leads vs. Impressions Scatter Plot',
                         labels={'Impressions': 'Total Impressions', 'Leads': 'Number of Leads'},
                         color_discrete_map={"Festival": "blue", "Offer": "orange"})
        st.plotly_chart(fig5, use_container_width=True)  

        # Correlation Matrix Calculation and Display
        numeric_cols = df.select_dtypes(include=np.number).columns  
        corr_matrix = df[numeric_cols].corr(method='pearson')

        # Display correlation matrix
        st.write("**Correlation Matrix:**")
        st.table(corr_matrix.style.background_gradient(cmap='coolwarm').format("{:.3f}"))


    except Exception as e:
        st.sidebar.error(f'Error: {e}. Please upload a valid CSV or Excel file with the correct columns.')




