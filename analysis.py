import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

# Set up the Streamlit page
st.title(':red[_RED_ _DOT_ _FOUNDATION_]')
st.sidebar.image("C:/Users/Admin/Desktop/Streamlit_dashboard/red_dot.jpg")  # Update with your actual image path

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Pre Session Analysis", "Post Session Analysis", "Summary"],
    )

# Color Palette
colors = ['rgb(55, 83, 109)', 'rgb(26, 118, 255)', 'rgb(144, 202, 249)']

if selected == "Pre Session Analysis":
    data = pd.read_excel("C:/Users/Admin/Desktop/Streamlit_dashboard/SafetyChampions1.xlsx")  # Update with your actual data path
    
    with st.sidebar:
        selected_1 = option_menu(
            menu_title="Pre Session Analysis Menu",
            options=["Demographics Analysis", "Questionnaire Analysis"],
        )

    if selected_1 == "Demographics Analysis":
        st.header("PRE SESSION ANALYSIS")
        col1, col2, col3 = st.columns(3)

        with col1:
            age_counts = data['Age'].value_counts().reset_index()
            age_counts.columns = ['Age', 'Count']
            fig = px.histogram(data, x='Age', nbins=20, title='Age Distribution')
            fig.update_traces(marker_color='rgb(144, 202, 249)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.8)
            fig.update_layout(
                xaxis_title='Age Group',
                yaxis_title='Number of Participants',
                bargap=0.1,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        with col2:
            gender_counts = data['Gender'].value_counts()
            fig = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, title='Gender Distribution',
                         hole=0.4, width=350, height=350)
            fig.update_traces(textinfo='percent+label', textfont_size=12, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        with col3:
            location_counts = data['Location'].value_counts().reset_index().head(10)
            location_counts.columns = ['Location', 'Count']
            fig = px.bar(location_counts, x='Location', y='Count', title='Top 10 Locations')
            fig.update_layout(
                xaxis={'categoryorder': 'total descending'},
                xaxis_title='Location',
                yaxis_title='Number of Participants',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        selected_location = st.selectbox("Select Location:", data['Location'].unique())

        # Filter Data by Location
        filtered_data = data[data['Location'] == selected_location]

        # Location-Specific Age Distribution
        age_counts = filtered_data['Age'].value_counts().reset_index()
        age_counts.columns = ['Age', 'Count']
        fig_age = px.histogram(filtered_data, x='Age', nbins=20, title=f'Age Distribution in {selected_location}')
        fig_age.update_traces(marker_color='rgb(144, 202, 249)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.8)
        fig_age.update_layout(
            xaxis_title='Age Group',
            yaxis_title='Number of Participants',
            bargap=0.1,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_age, use_container_width=True, theme="streamlit")
        
        # Location-Specific Gender Distribution
        gender_counts = filtered_data['Gender'].value_counts()
        fig_gender = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, title='Gender Distribution', hole=0.4, width=350, height=350)
        fig_gender.update_traces(textinfo='percent+label', textfont_size=12, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
        fig_gender.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="left",
                x=0
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_gender, use_container_width=True, theme="streamlit")
        
    elif selected_1 == "Questionnaire Analysis":
        st.header("PRE SESSION ANALYSIS")
        tol1, tol2 = st.columns(2)
        with tol1:
            willing_counts = data['Willingness to Volunteer'].value_counts()
            fig = px.pie(
                willing_counts,
                values=willing_counts.values,
                names=willing_counts.index,
                title='Willingness to Volunteer',
                hole=0.4,
                width=400,
                height=400
            )
            fig.update_traces(
                textposition='inside',
                textinfo='percent+label',
                textfont_size=14,
                marker=dict(
                    colors=colors,
                    line=dict(color='#000000', width=2)
                ),
                pull=[0.05] * len(willing_counts)
            )
            fig.update_layout(
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        with tol2:
            download_counts = data['I have downloaded the safecity app'].value_counts()
            fig = px.pie(
                download_counts,
                values=download_counts.values,
                names=download_counts.index,
                title='I have downloaded the safecity app',
                hole=0.4,
                width=400,
                height=400
            )
            fig.update_traces(
                textposition='inside',
                textinfo='percent+label',
                textfont_size=14,
                marker=dict(
                    colors=colors,
                    line=dict(color='#000000', width=2)
                ),
                pull=[0.05] * len(download_counts)
            )
            fig.update_layout(
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

elif selected == "Post Session Analysis":
    data = pd.read_excel("C:/Users/Admin/Desktop/Streamlit_dashboard/Feedback2021.xlsx")  # Update with your actual data path
    st.header("POST SESSION ANALYSIS")

    with st.sidebar:
        selected_2 = option_menu(
            menu_title="Post Session Analysis Menu",
            options=["Demographics Analysis", "Questionnaire Analysis"],
        )

    if selected_2 == "Demographics Analysis":
        col1, col2, col3 = st.columns(3)
        with col1:
            age_counts = data['Age'].value_counts().reset_index()
            age_counts.columns = ['Age', 'Count']
            fig = px.histogram(data, x='Age', nbins=20, title='Age Distribution')
            fig.update_traces(marker_color='rgb(144, 202, 249)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.8)
            fig.update_layout(
                xaxis_title='Age Group',
                yaxis_title='Number of Participants',
                bargap=0.1,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        with col2:
            gender_counts = data['Gender'].value_counts()
            fig = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, title='Gender Distribution',hole=0.4, width=350, height=350)
            fig.update_traces(textinfo='percent+label', textfont_size=12, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        with col3:
            location_counts = data['Location'].value_counts().reset_index().head(10)
            location_counts.columns = ['Location', 'Count']
            fig = px.bar(location_counts, x='Location', y='Count', title='Top 10 Locations')
            fig.update_layout(
                xaxis={'categoryorder': 'total descending'},
                xaxis_title='Location',
                yaxis_title='Number of Participants',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")

        selected_location = st.selectbox("Select Location:", data['Location'].unique())

        # Filter Data by Location
        filtered_data = data[data['Location'] == selected_location]

        # Location-Specific Age Distribution
        age_counts = filtered_data['Age'].value_counts().reset_index()
        age_counts.columns = ['Age', 'Count']
        fig_age = px.histogram(filtered_data, x='Age', nbins=20, title=f'Age Distribution in {selected_location}')
        fig_age.update_traces(marker_color='rgb(144, 202, 249)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.8)
        fig_age.update_layout(
            xaxis_title='Age Group',
            yaxis_title='Number of Participants',
            bargap=0.1,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_age, use_container_width=True, theme="streamlit")

        # Location-Specific Gender Distribution
        gender_counts = filtered_data['Gender'].value_counts()
        fig_gender = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, title=f'Gender Distribution', hole=0.4, width=350, height=350)
        fig_gender.update_traces(textinfo='percent+label', textfont_size=12, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
        fig_gender.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="left",
                x=0
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_gender, use_container_width=True, theme="streamlit")


    elif selected_2 == "Questionnaire Analysis":

        questions = [
            "Satisfaction Level with Champion Campaign",
            "Rating of Orientation Sessions",
            "Rating of Campaign Activities",
            "Rating the Support throughout the Campaign",
            "Rating the ease of using the Safecity platform",
            "Recommending Safecity to friends"
        ]
        tol1, tol2 = st.columns(2)
        
        for i, question in enumerate(questions):
            with (tol1 if i % 2 == 0 else tol2):
                question_counts = data[question].value_counts()
                fig = px.pie(
                    question_counts,
                    values=question_counts.values,
                    names=question_counts.index,
                    title=question,
                    hole=0.4,
                    width=400,
                    height=400
                )
                fig.update_traces(
                    textposition='inside',
                    textinfo='percent+label',
                    textfont_size=14,
                    marker=dict(
                        colors=colors,
                        line=dict(color='#000000', width=2)
                    ),
                    pull=[0.05] * len(question_counts)
                )
                fig.update_layout(
                    showlegend=True,
                    legend=dict(
                        orientation="h",
                        yanchor="top",
                        y=1.02,
                        xanchor="left",
                        x=1
                    ),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True, theme="streamlit")

elif selected =="Summary":
        st.header("SUMMARY")
        data = pd.read_excel("C:/Users/Admin/Desktop/Streamlit_dashboard/Feedback2021.xlsx")  # Update with your actual data path
        questions = [
            "Rate your knowlege prior",
            "Rate your knowledge post campaign",
            "Rate the knowledge of people",
            "Would you consider the Safecity app friendly?"
        ]
        tol1, tol2 = st.columns(2)
        for i, question in enumerate(questions):
            with (tol1 if i % 2 == 0 else tol2):
                question_counts = data[question].value_counts()
                fig = px.pie(
                    question_counts,
                    values=question_counts.values,
                    names=question_counts.index,
                    title=question,
                    hole=0.4,
                    width=400,
                    height=400
                )
                fig.update_traces(
                    textposition='inside',
                    textinfo='percent+label',
                    textfont_size=14,
                    marker=dict(
                        colors=colors,
                        line=dict(color='#000000', width=2)
                    ),
                    pull=[0.05] * len(question_counts)
                )
                fig.update_layout(
                    showlegend=True,
                    legend=dict(
                        orientation="h",
                        yanchor="top",
                        y=1.02,
                        xanchor="left",
                        x=1
                    ),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True, theme="streamlit")
        with st.expander("See explanation"):
            st.write(''' From the first two pie diagram we can see that before the session 58.8 % of the respondents were somewhat aware and post the session the 
             percentage decreased to 21.5 % , which means a total percentage change of 63.4% . This change has mostly been converted to the respondents being 
             fully aware as the percentage of totally aware before the seesion was 39.5% and post the session it rose up to 77.9% , showing a percentage change 
             of 97.2%. This shows that there has been a significant impact of the session on the respondents.''')
