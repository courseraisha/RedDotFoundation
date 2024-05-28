#Install all these packages 
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# TITLE
st.title("RED DOT FOUNDATION - SURVEY ANALYSIS")
st.sidebar.title("Language Selection")
language = st.sidebar.selectbox("Select an option", ["HINDI FEEDBACK ANALYSIS", "ENGLISH FEEDBACK ANALYSIS"])
if language == 'HINDI FEEDBACK ANALYSIS':
    data = pd.read_excel('HINDI.xlsx')
elif language == 'ENGLISH FEEDBACK ANALYSIS':
    data = pd.read_excel('EnglishFeedback.xlsx')
# Load the data based on the selected language

def generate_respondents_plotsH(data, plot_type):
    if plot_type == "Gender Distribution":
        gender_count = data['gender'].value_counts(normalize=True).reset_index()
        gender_count.columns = ['gender', 'count']
        fig = px.bar(gender_count, x='gender', y='count', title='Gender Distribution', color='gender', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Age Group Distribution':
        age_counts = data['Age'].value_counts(normalize=True).reset_index()
        age_counts.columns = ['Age', 'count']
        fig = px.pie(age_counts, names='Age', values='count', title='Age Group Distribution')
        st.plotly_chart(fig)

    elif plot_type == 'Organization Distribution':
        org_counts = data['Name of Organization/Institute'].value_counts(normalize=True).reset_index()
        org_counts.columns = ['Name of Organization/Institute','count']
        fig = px.bar(org_counts, x='Name of Organization/Institute', y='count', title='Organization Distribution', color='Name of Organization/Institute', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Place Distribution':
        place_counts = data['place'].value_counts(normalize=True).reset_index()
        place_counts.columns = ['place','count']
        fig = px.bar(place_counts, x='place', y='count', title='Place Distribution', color='place', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Understanding Levels':
        understanding_columns = [
            'I have a good understanding of what abusive behavior and street harassment looks like.',
            'I have a deep understanding of the impact that abusive behavior and street harassment has on people.'
        ]
        for col in understanding_columns:
            understanding_counts = data[col].value_counts(normalize=True).reset_index()
            understanding_counts.columns = [col, 'count']
            fig = px.bar(understanding_counts, x=col, y='count', title=col, color=col, text='count')
            fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

    elif plot_type == 'Instructor Evaluation':
        knowledge_counts = data['The instructor was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
        knowledge_counts.columns = ['Knowledge Level', 'count']
        engagement_counts = data['The instructor was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
        engagement_counts.columns = ['Engagement Level', 'count']
        fig_knowledge = px.bar(knowledge_counts, x='Knowledge Level', y='count', title='Instructor Knowledge Levels', color='Knowledge Level', text='count')
        fig_knowledge.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig_knowledge.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig_engagement = px.bar(engagement_counts, x='Engagement Level', y='count', title='Instructor Engagement Levels', color='Engagement Level', text='count')
        fig_engagement.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig_engagement.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_knowledge)
        st.plotly_chart(fig_engagement)

def generate_trainer_plotsH(trainer_data):
    present_count = trainer_data['The presentation was easy to understand.'].value_counts(normalize=True).reset_index()
    present_count.columns = ['The presentation was easy to understand.', 'count']
    fig = px.bar(present_count, x='The presentation was easy to understand.', y='count', title='Ease in Understanding the Presentation', color='The presentation was easy to understand.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    knowledge_counts = trainer_data['The instructor was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
    knowledge_counts.columns = ['The instructor was knowledgeable and prepared.', 'count']
    fig = px.bar(knowledge_counts, x='The instructor was knowledgeable and prepared.', y='count', title='Instructor Knowledge Levels', color='The instructor was knowledgeable and prepared.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    engagement_counts = trainer_data['The instructor was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
    engagement_counts.columns = ['The instructor was engaging and encouraged participation.', 'count']
    fig = px.bar(engagement_counts, x='The instructor was engaging and encouraged participation.', y='count', title='Instructor Engagement Levels', color='The instructor was engaging and encouraged participation.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def generate_respondents_plotsE(data, plot_type):
    if plot_type == "Gender Distribution":
        gender_count = data['Gender'].value_counts(normalize=True).reset_index()
        gender_count.columns = ['Gender', 'count']
        fig = px.bar(gender_count, x='Gender', y='count', title='Gender Distribution', color='Gender', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Age Group Distribution':
        age_counts = data['Age'].value_counts(normalize=True).reset_index()
        age_counts.columns = ['Age', 'count']
        fig = px.pie(age_counts, names='Age', values='count', title='Age Group Distribution')
        st.plotly_chart(fig)

    elif plot_type == 'Organization Distribution':
        org_counts = data['Name of Organization / Institution '].value_counts(normalize=True).reset_index()
        org_counts.columns = ['Name of Organization / Institution ','count']
        fig = px.bar(org_counts, x='Name of Organization / Institution ', y='count', title='Organization Distribution', color='Name of Organization / Institution ', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Place Distribution':
        place_counts = data['Location '].value_counts(normalize=True).reset_index()
        place_counts.columns = ['Location ','count']
        fig = px.bar(place_counts, x='Location ', y='count', title='Place Distribution', color='Location ', text='count')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Understanding Levels':
        understanding_columns = [
            'I have a strong understanding of what disrespectful behaviour and street harassment looks like.',
            ' I have a strong understanding of what impact disrespectful behaviour and street harassment has on people.',
            'The 5Ds provide strategies for me to safely intervene when I witness street harassment.',
            'I am confident that I would intervene if I saw disrespect or harassment.',
            'I feel more prepared to respond, either in the moment or afterwards by taking care of myself, the next time I experience harassment.',
            'The scenarios gave me an opportunity to practice applying the new strategies I learned today.'
        ]
        for col in understanding_columns:
            understanding_counts = data[col].value_counts(normalize=True).reset_index()
            understanding_counts.columns = [col, 'count']
            fig = px.bar(understanding_counts, x=col, y='count', title=col, color=col, text='count')
            fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

    elif plot_type == 'Instructor Evaluation':
        knowledge_counts = data['The trainer was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
        knowledge_counts.columns = ['Knowledge Level', 'count']
        engagement_counts = data['The trainer was engaging and encouraged participation.'].value_counts().reset_index()
        engagement_counts.columns = ['Engagement Level', 'count']
        fig_knowledge = px.bar(knowledge_counts, x='Knowledge Level', y='count', title='Instructor Knowledge Levels', color='Knowledge Level', text='count')
        fig_knowledge.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig_knowledge.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig_engagement = px.bar(engagement_counts, x='Engagement Level', y='count', title='Instructor Engagement Levels', color='Engagement Level', text='count')
        fig_engagement.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig_engagement.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_knowledge)
        st.plotly_chart(fig_engagement)


def generate_trainer_plotsE(trainer_data):
    present_count = trainer_data['The presentation was easy to understand.'].value_counts(normalize=True).reset_index()
    present_count.columns = ['The presentation was easy to understand.', 'count']
    fig = px.bar(present_count, x='The presentation was easy to understand.', y='count', title='Ease in Understanding the Presentation', color='The presentation was easy to understand.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    knowledge_counts = trainer_data['The trainer was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
    knowledge_counts.columns = ['The trainer was knowledgeable and prepared.', 'count']
    fig = px.bar(knowledge_counts, x='The trainer was knowledgeable and prepared.', y='count', title='Instructor Knowledge Levels', color='The trainer was knowledgeable and prepared.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    engagement_counts = trainer_data['The trainer was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
    engagement_counts.columns = ['The trainer was engaging and encouraged participation.', 'count']
    fig = px.bar(engagement_counts, x='The trainer was engaging and encouraged participation.', y='count', title='Instructor Engagement Levels', color='The trainer was engaging and encouraged participation.', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

# Language Wise Analysis
if language == "HINDI FEEDBACK ANALYSIS":
    st.sidebar.title("Analysis Selection")
    analysis_type = st.sidebar.selectbox("Choose analysis type:", ['Respondents', 'Trainer'])
    
    if analysis_type == 'Respondents':
        st.subheader("Respondents Analysis")
        plot_type = st.selectbox("Choose a plot type:", ['Gender Distribution', 'Age Group Distribution', 'Organization Distribution', 'Place Distribution', 'Understanding Levels', 'Instructor Evaluation'])
        generate_respondents_plotsH(data, plot_type)
    
    elif analysis_type == 'Trainer':
        st.subheader("Trainer Analysis")
        trainer = st.selectbox("Choose a trainer:", ['Jyoti Goyal', 'Pragati Vaishya', 'Glorious Mahske', 'Ritu Verma', 'Sonali Alves'])
        trainer_data = data[data['name of instructor'] == trainer]
        if not trainer_data.empty:
            generate_trainer_plotsH(trainer_data)
        else:
            st.write("No data available for the selected trainer.")

elif language == 'ENGLISH FEEDBACK ANALYSIS':
    st.sidebar.title("Analysis Selection")
    analysis_type = st.sidebar.selectbox("Choose analysis type:", ['Respondents', 'Trainer'])
    
    if analysis_type == 'Respondents':
        st.subheader("Respondents Analysis")
        plot_type = st.selectbox("Choose a plot type:", ['Gender Distribution', 'Age Group Distribution', 'Organization Distribution', 'Place Distribution', 'Understanding Levels', 'Instructor Evaluation'])
        generate_respondents_plotsE(data, plot_type)
    
    elif analysis_type == 'Trainer':
        st.subheader("Trainer Analysis")
        trainer = st.selectbox("Choose a trainer:", ['Jyoti Goyal', 'Pragati Vaishya', 'Ritu Verma', 'Sonali Alves', 'Kiran Saju', 'Monika Rajashekhar', 'Nisha Kumari', 'Shital Vidhate', 'Tehsin Shaikh', 'Vaibhavi Rani'])
        trainer_data = data[data['Trainers Name '] == trainer]
        if not trainer_data.empty:
            generate_trainer_plotsE(trainer_data)
        else:
            st.write("No data available for the selected trainer.")
