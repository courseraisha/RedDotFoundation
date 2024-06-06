import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime

st.set_page_config(layout="wide")

st.title(":orange[_SPAN COMMUNICATIONS_]")
selected_option = st.sidebar.selectbox("Select an option", ["December Daily Report", "January Performance Leads"])

if selected_option == "December Daily Report":
    data = pd.read_excel("DEC_DAILY_REPORT.xlsx")
    
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Scaling Numeric Columns
    scaler = MinMaxScaler()
    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    # Add back the 'Date' column for plotting later
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Multi-line graph for Impressions and Clicks
    df_impressions_clicks = data[['Date', 'Impressions', 'Clicks']]
    df_impressions_clicks_melted = df_impressions_clicks.melt(id_vars='Date', value_vars=['Impressions', 'Clicks'], var_name='Metric', value_name='Scaled Value')
    
    fig1 = px.line(df_impressions_clicks_melted, x='Date', y='Scaled Value', color='Metric', title='Impressions and Clicks Over Time', markers=True)
    fig1.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""
        **Analysis:**

        - **Overall Trend**: Both Impressions and Clicks show a general upward trend throughout December, indicating increasing engagement.
        - **Early December**: Initially there is a significant rise on 9 December.
        - **Mid-December Fluctuations**: Variations between December 12 and December 21 could be due to different campaign intensities or user behavior.
        - **Late December Increase**: Significant spike around December 24 to December 27, likely due to holiday season activities.
        - **End-of-Month Decline**: Sharp decline after December 27 might be due to reduced online activity during the holiday break.
        """)
    
    # Multi-line graph for Leads and CPL
    df_leads_cpl = data[['Date', 'Leads', 'CPL']]
    df_leads_cpl_melted = df_leads_cpl.melt(id_vars='Date', value_vars=['Leads', 'CPL'], var_name='Metric', value_name='Scaled Value')
    fig2 = px.line(df_leads_cpl_melted, x='Date', y='Scaled Value', color='Metric', title='Leads and CPL Over Time', markers=True)
    fig2.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig2, use_container_width=True)
    st.write("""
        **Analysis:**

        - **Overall Trend**: Both Leads and Cost Per Lead (CPL) show varying trends throughout December, reflecting changes in user engagement and campaign performance.
        - **Early December**: There is a significant spike in both Leads and CPL around December 9 indicating the launch of a new campaign or promotional activity.
        - **Mid-December Stability**: Relative stability with fluctuations between December 12 and December 23 suggests the maintenance phase of ongoing campaigns.
        - **Late December Increase**: Noticeable increase in Leads around December 24 to December 27 likely corresponds to holiday season activities and promotions.
        - **End-of-Month Decline**: Sharp decline towards the end of December after December 27 could be attributed to the winding down of holiday campaigns or reduced online activity.
        """)
    
    # Scatter Plot of Leads (or Calls) vs Impressions
    fig5 = px.scatter(data, x='Impressions', y='Leads', title='Leads vs. Impressions Scatter Plot', labels={'Impressions': 'Total Impressions', 'Leads': 'Number of Leads'}, color_discrete_map={"Festival": "blue", "Offer": "orange"})
    st.plotly_chart(fig5, use_container_width=True)  
    st.write("""
        **Analysis:**

        - **Positive Relationship**: There is a general weak relationship between the number of impressions and the number of leads.
        - **Density of Data Points**: Most data points are clustered in the middle range of impressions and leads, indicating moderate engagement.
        """)
    # Correlation Matrix Calculation and Display
    corr_matrix = data[numeric_cols].corr(method='pearson')
    
    # Display correlation matrix
    st.write("**Correlation Matrix:**")
    st.table(corr_matrix.style.background_gradient(cmap='coolwarm').format("{:.3f}"))
    st.write("""
**Analysis:**

- **Positive Correlations:**
   - Impressions and Clicks (0.907): More impressions lead to more clicks, showcasing ad effectiveness.
   - Impressions and Amount Spent (0.983): Increased spending yields wider reach.
   - Clicks and Amount Spent (0.948): Higher spending is linked to increased clicks.
   - Clicks and Leads (0.798): More clicks result in more leads, demonstrating campaign effectiveness.

- **Negative Correlations:**
   - CTR% and CPL (-0.741): Engaging ads with higher CTR are more cost-effective.
   - Leads and CPL (-0.667): More leads generally lead to a lower cost per lead, likely due to economies of scale.

- **Weak Correlations:**
   - CPL and Amount Spent (-0.040): Increasing budget doesn't guarantee lower cost per lead. 
""")
if selected_option == "January Performance Leads":
    data = pd.read_excel("JAN_PERFORMANCE_LEADS.xlsx")
    
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Scaling Numeric Columns
    scaler = MinMaxScaler()
    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    
    # Add back the 'Date' column for plotting later
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # Multi-line graph for Impressions and Clicks
    df_impressions_clicks = data[['Date', 'Impressions', 'Clicks']]
    df_impressions_clicks_melted = df_impressions_clicks.melt(id_vars='Date', value_vars=['Impressions', 'Clicks'], var_name='Metric', value_name='Scaled Value')
    
    fig1 = px.line(df_impressions_clicks_melted, x='Date', y='Scaled Value', color='Metric', title='Impressions and Clicks Over Time', markers=True)
    fig1.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""
        **Analysis:**

        - **Overall Trend**: Both Impressions and Clicks shows fluctuations in the trend throughoutthe month.
        - **Early January**: Initially there is a rise in the trend and then there is a short setback.
        - **Mid-January Fluctuations**: There is a significant increase from 17 Jan until it reaches its peak on 20 Jan.
        - **End-of-Month Decline**: Significant decline can be seen after 20 Jan, even after an increase in the Impressions there could not have been an increase in Clicks.
        """)
    
    # Multi-line graph for Leads and CPL
    df_leads_cpl = data[['Date', 'Leads', 'CPL']]
    df_leads_cpl_melted = df_leads_cpl.melt(id_vars='Date', value_vars=['Leads', 'CPL'], var_name='Metric', value_name='Scaled Value')
    fig2 = px.line(df_leads_cpl_melted, x='Date', y='Scaled Value', color='Metric', title='Leads and CPL Over Time', markers=True)
    fig2.update_layout(xaxis_title='Date', yaxis_title='Scaled Value', legend_title_text='Metric')
    st.plotly_chart(fig2, use_container_width=True)
    st.write("""
        **Analysis:**

        - **Overall Trend**: Both Leads and Cost Per Lead (CPL) show varying trends throughout January, reflecting changes in user engagement and campaign performance.
        - **Early January**: There is a significant spike in both Leads and CPL around December 9 indicating the launch of a new campaign or promotional activity.
        - **Mid-January Stability**: Relative stability in the CPL with fluctuations in the Leads.
        - **End-of-Month Decline**: Sharp decline in the Leads towards the end of January after December 21 and high CPL .
        """)
    
    # Scatter Plot of Leads (or Calls) vs Impressions
    fig5 = px.scatter(data, x='Impressions', y='Leads', title='Leads vs. Impressions Scatter Plot', labels={'Impressions': 'Total Impressions', 'Leads': 'Number of Leads'}, color_discrete_map={"Festival": "blue", "Offer": "orange"})
    st.plotly_chart(fig5, use_container_width=True)  
    st.write("""
        **Analysis:**

        - **Positive Relationship**: There is a moderate relationship between the number of impressions and the number of leads.
        - **Density of Data Points**: The relationship is not perfectly linear, as the data points are scattered and do not form a straight line.
        """)
    # Correlation Matrix Calculation and Display
    corr_matrix = data[numeric_cols].corr(method='pearson')
    
    # Display correlation matrix
    st.write("**Correlation Matrix:**")
    st.table(corr_matrix.style.background_gradient(cmap='coolwarm').format("{:.3f}"))
    st.write("""
**Analysis:**

**Positive Correlations:**

* **Impressions and Clicks (0.843):** Strong positive relationship, indicating as impressions increase, clicks tend to increase, suggesting effective ads.
* **Impressions and Amount Spent (0.990):** Very strong positive correlation, higher spending leads to more impressions, expanding reach.
* **Clicks and Amount Spent (0.878):** Strong positive correlation, increased spending leads to more clicks.
* **Clicks and Leads (0.922):** Very strong positive correlation, ads with more clicks are likely to generate more leads, effective in driving interest.

**Negative Correlations:**

* **CTR% and CPL (-0.640):** Engaging ads with higher CTR are more cost-effective.
* **Leads and CPL (-0.588):** More leads generally lead to a lower cost per lead, likely due to economies of scale.

**Weak Correlations:**

* **Impressions and CPL (-0.006), CPL and Amount Spent (-0.009):** Increasing budget doesn't guarantee lower or higher cost per lead. 
* **CTR% and Amount Spent (-0.346):** More spending doesn't always result in higher click-through rate, indicating other factors at play.
""")


