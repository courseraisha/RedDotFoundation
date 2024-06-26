import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# TITLE
st.title("RED DOT FOUNDATION - SURVEY ANALYSIS")
st.sidebar.title("Language Selection")
language = st.sidebar.selectbox("Select an option", ["HINDI FEEDBACK ANALYSIS", "ENGLISH FEEDBACK ANALYSIS","MARATHI FEEDBACK ANALYSIS"])

if language == 'HINDI FEEDBACK ANALYSIS':
    data = pd.read_excel('HINDI.xlsx')
elif language == 'ENGLISH FEEDBACK ANALYSIS':
    data = pd.read_excel('EnglishFeedback.xlsx')
elif language == 'MARATHI FEEDBACK ANALYSIS':
    data = pd.read_excel('MARATHI.xlsx')
# Load the data based on the selected language

def generate_respondents_plotsH(data, plot_type):
    if plot_type == "Gender Distribution":
        gender_count = data['gender'].value_counts(normalize=True).reset_index()
        gender_count.columns = ['gender', 'percentage']
        gender_count['percentage'] *= 100
        fig = px.bar(gender_count, x='gender', y='percentage', title='Gender Distribution', color='gender', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Age Group Distribution':
        age_counts = data['Age'].value_counts(normalize=True).reset_index()
        age_counts.columns = ['Age', 'percentage']
        age_counts['percentage'] *= 100
        fig = px.pie(age_counts, names='Age', values='percentage', title='Age Group Distribution')
        st.plotly_chart(fig)

    elif plot_type == 'Organization Distribution':
        org_counts = data['Name of Organization/Institute'].value_counts(normalize=True).reset_index()
        org_counts.columns = ['Name of Organization/Institute', 'percentage']
        org_counts['percentage'] *= 100
        fig = px.bar(org_counts, x='Name of Organization/Institute', y='percentage', title='Organization Distribution', color='Name of Organization/Institute', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Place Distribution':
        place_counts = data['place'].value_counts(normalize=True).reset_index()
        place_counts.columns = ['place', 'percentage']
        place_counts['percentage'] *= 100
        fig = px.bar(place_counts, x='place', y='percentage', title='Place Distribution', color='place', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Understanding Levels':
        understanding_columns = [
            'I have a good understanding of what abusive behavior and street harassment looks like.',
            'I have a deep understanding of the impact that abusive behavior and street harassment has on people.'
        ]
        for col in understanding_columns:
            understanding_counts = data[col].value_counts(normalize=True).reset_index()
            understanding_counts.columns = [col, 'percentage']
            understanding_counts['percentage'] *= 100
            fig = px.bar(understanding_counts, x=col, y='percentage', title=col, color=col, text='percentage')
            fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

    elif plot_type == 'Instructor Evaluation':
        knowledge_counts = data['The instructor was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
        knowledge_counts.columns = ['Knowledge Level', 'percentage']
        knowledge_counts['percentage'] *= 100
        engagement_counts = data['The instructor was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
        engagement_counts.columns = ['Engagement Level', 'percentage']
        engagement_counts['percentage'] *= 100
        fig_knowledge = px.bar(knowledge_counts, x='Knowledge Level', y='percentage', title='Instructor Knowledge Levels', color='Knowledge Level', text='percentage')
        fig_knowledge.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_knowledge.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig_engagement = px.bar(engagement_counts, x='Engagement Level', y='percentage', title='Instructor Engagement Levels', color='Engagement Level', text='percentage')
        fig_engagement.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_engagement.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_knowledge)
        st.plotly_chart(fig_engagement)

def generate_trainer_plotsH(trainer_data):
    present_count = trainer_data['The presentation was easy to understand.'].value_counts(normalize=True).reset_index()
    present_count.columns = ['The presentation was easy to understand.', 'percentage']
    present_count['percentage'] *= 100
    fig = px.bar(present_count, x='The presentation was easy to understand.', y='percentage', title='Ease in Understanding the Presentation', color='The presentation was easy to understand.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    knowledge_counts = trainer_data['The instructor was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
    knowledge_counts.columns = ['The instructor was knowledgeable and prepared.', 'percentage']
    knowledge_counts['percentage'] *= 100
    fig = px.bar(knowledge_counts, x='The instructor was knowledgeable and prepared.', y='percentage', title='Instructor Knowledge Levels', color='The instructor was knowledgeable and prepared.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    engagement_counts = trainer_data['The instructor was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
    engagement_counts.columns = ['The instructor was engaging and encouraged participation.', 'percentage']
    engagement_counts['percentage'] *= 100
    fig = px.bar(engagement_counts, x='The instructor was engaging and encouraged participation.', y='percentage', title='Instructor Engagement Levels', color='The instructor was engaging and encouraged participation.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def generate_respondents_plotsE(data, plot_type):
    if plot_type == "Gender Distribution":
        gender_count = data['Gender'].value_counts(normalize=True).reset_index()
        gender_count.columns = ['Gender', 'percentage']
        gender_count['percentage'] *= 100
        fig = px.bar(gender_count, x='Gender', y='percentage', title='Gender Distribution', color='Gender', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Age Group Distribution':
        age_counts = data['Age'].value_counts(normalize=True).reset_index()
        age_counts.columns = ['Age', 'percentage']
        age_counts['percentage'] *= 100
        fig = px.pie(age_counts, names='Age', values='percentage', title='Age Group Distribution')
        st.plotly_chart(fig)

    elif plot_type == 'Organization Distribution':
        org_counts = data['Name of Organization / Institution '].value_counts(normalize=True).reset_index()
        org_counts.columns = ['Name of Organization / Institution ', 'percentage']
        org_counts['percentage'] *= 100
        fig = px.bar(org_counts, x='Name of Organization / Institution ', y='percentage', title='Organization Distribution', color='Name of Organization / Institution ', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Place Distribution':
        place_counts = data['Location '].value_counts(normalize=True).reset_index()
        place_counts.columns = ['Location ', 'percentage']
        place_counts['percentage'] *= 100
        fig = px.bar(place_counts, x='Location ', y='percentage', title='Place Distribution', color='Location ', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
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
            understanding_counts.columns = [col, 'percentage']
            understanding_counts['percentage'] *= 100
            fig = px.bar(understanding_counts, x=col, y='percentage', title=col, color=col, text='percentage')
            fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

    elif plot_type == 'Instructor Evaluation':
        knowledge_counts = data['The trainer was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
        knowledge_counts.columns = ['Knowledge Level', 'percentage']
        knowledge_counts['percentage'] *= 100
        engagement_counts = data['The trainer was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
        engagement_counts.columns = ['Engagement Level', 'percentage']
        engagement_counts['percentage'] *= 100
        fig_knowledge = px.bar(knowledge_counts, x='Knowledge Level', y='percentage', title='Instructor Knowledge Levels', color='Knowledge Level', text='percentage')
        fig_knowledge.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_knowledge.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig_engagement = px.bar(engagement_counts, x='Engagement Level', y='percentage', title='Instructor Engagement Levels', color='Engagement Level', text='percentage')
        fig_engagement.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_engagement.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_knowledge)
        st.plotly_chart(fig_engagement)


def generate_trainer_plotsE(trainer_data):
    present_count = trainer_data['The presentation was easy to understand.'].value_counts(normalize=True).reset_index()
    present_count.columns = ['The presentation was easy to understand.', 'percentage']
    present_count['percentage'] *= 100
    fig = px.bar(present_count, x='The presentation was easy to understand.', y='percentage', title='Ease in Understanding the Presentation', color='The presentation was easy to understand.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    knowledge_counts = trainer_data['The trainer was knowledgeable and prepared.'].value_counts(normalize=True).reset_index()
    knowledge_counts.columns = ['The trainer was knowledgeable and prepared.', 'percentage']
    knowledge_counts['percentage'] *= 100
    fig = px.bar(knowledge_counts, x='The trainer was knowledgeable and prepared.', y='percentage', title='Instructor Knowledge Levels', color='The trainer was knowledgeable and prepared.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    engagement_counts = trainer_data['The trainer was engaging and encouraged participation.'].value_counts(normalize=True).reset_index()
    engagement_counts.columns = ['The trainer was engaging and encouraged participation.', 'percentage']
    engagement_counts['percentage'] *= 100
    fig = px.bar(engagement_counts, x='The trainer was engaging and encouraged participation.', y='percentage', title='Instructor Engagement Levels', color='The trainer was engaging and encouraged participation.', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def generate_respondents_plotsM(data, plot_type):
    if plot_type == "Gender Distribution":
        gender_count = data['Gender'].value_counts(normalize=True).reset_index()
        gender_count.columns = ['Gender', 'percentage']
        gender_count['percentage'] *= 100
        fig = px.bar(gender_count, x='Gender', y='percentage', title='Gender Distribution', color='Gender', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Age Group Distribution':
        age_counts = data['Age'].value_counts(normalize=True).reset_index()
        age_counts.columns = ['Age', 'percentage']
        age_counts['percentage'] *= 100
        fig = px.pie(age_counts, names='Age', values='percentage', title='Age Group Distribution')
        st.plotly_chart(fig)

    elif plot_type == 'Organization Distribution':
        org_counts = data['Name of Organization/Institute'].value_counts(normalize=True).reset_index()
        org_counts.columns = ['Name of Organization/Institute', 'percentage']
        org_counts['percentage'] *= 100
        fig = px.bar(org_counts, x='Name of Organization/Institute', y='percentage', title='Organization Distribution', color='Name of Organization/Institute', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Place Distribution':
        place_counts = data['place'].value_counts(normalize=True).reset_index()
        place_counts.columns = ['place', 'percentage']
        place_counts['percentage'] *= 100
        fig = px.bar(place_counts, x='place', y='percentage', title='Place Distribution', color='place', text='percentage')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig)

    elif plot_type == 'Understanding Levels':
        understanding_columns = [
            'I have a strong understanding of what disrespectful behavior and street harassment looks like',
            'I strongly understand the impact of abusive behavior and street harassment on people',
            'When I see street harassment, the 5Ds provides me with strategies to safely intervene',
            'I believe I will intervene if I see disrespect or harassment',
            'The next time I experience harassment, I feel more prepared to respond by taking care of myself in the moment or later',
            'The situation gave me an opportunity to practice applying the new strategies I learned today',
            'If I walk out here today and see harassment happening on the street, I think there is at least one thing I can do to intervene',
            'I would recommend this training to a friend or colleague'
        ]
        for col in understanding_columns:
            understanding_counts = data[col].value_counts(normalize=True).reset_index()
            understanding_counts.columns = [col, 'percentage']
            understanding_counts['percentage'] *= 100
            fig = px.bar(understanding_counts, x=col, y='percentage', title=col, color=col, text='percentage')
            fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            st.plotly_chart(fig)

    elif plot_type == 'Instructor Evaluation':
        knowledge_counts = data['The instructor was knowledgeable and prepared'].value_counts(normalize=True).reset_index()
        knowledge_counts.columns = ['Knowledge Level', 'percentage']
        knowledge_counts['percentage'] *= 100
        engagement_counts = data['The instructor was engaging and encouraged participation'].value_counts(normalize=True).reset_index()
        engagement_counts.columns = ['Engagement Level', 'percentage']
        engagement_counts['percentage'] *= 100
        fig_knowledge = px.bar(knowledge_counts, x='Knowledge Level', y='percentage', title='Instructor Knowledge Levels', color='Knowledge Level', text='percentage')
        fig_knowledge.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_knowledge.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig_engagement = px.bar(engagement_counts, x='Engagement Level', y='percentage', title='Instructor Engagement Levels', color='Engagement Level', text='percentage')
        fig_engagement.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_engagement.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_knowledge)
        st.plotly_chart(fig_engagement)


def generate_trainer_plotsM(trainer_data):
    present_count = trainer_data['The presentation was easy to understand'].value_counts(normalize=True).reset_index()
    present_count.columns = ['The presentation was easy to understand', 'percentage']
    present_count['percentage'] *= 100
    fig = px.bar(present_count, x='The presentation was easy to understand', y='percentage', title='Ease in Understanding the Presentation', color='The presentation was easy to understand', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    knowledge_counts = trainer_data['The instructor was knowledgeable and prepared'].value_counts(normalize=True).reset_index()
    knowledge_counts.columns = ['The instructor was knowledgeable and prepared', 'percentage']
    knowledge_counts['percentage'] *= 100
    fig = px.bar(knowledge_counts, x='The instructor was knowledgeable and prepared', y='percentage', title='Instructor Knowledge Levels', color='The instructor was knowledgeable and prepared', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

    engagement_counts = trainer_data['The instructor was engaging and encouraged participation'].value_counts(normalize=True).reset_index()
    engagement_counts.columns = ['The instructor was engaging and encouraged participation', 'percentage']
    engagement_counts['percentage'] *= 100
    fig = px.bar(engagement_counts, x='The instructor was engaging and encouraged participation', y='percentage', title='Instructor Engagement Levels', color='The instructor was engaging and encouraged participation', text='percentage')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
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
            
elif language == 'MARATHI FEEDBACK ANALYSIS':
    st.sidebar.title("Analysis Selection")
    analysis_type = st.sidebar.selectbox("Choose analysis type:", ['Respondents', 'Trainer'])
    
    if analysis_type == 'Respondents':
        st.subheader("Respondents Analysis")
        plot_type = st.selectbox("Choose a plot type:", ['Gender Distribution', 'Age Group Distribution', 'Organization Distribution', 'Place Distribution', 'Understanding Levels', 'Instructor Evaluation'])
        generate_respondents_plotsM(data, plot_type)
    
    elif analysis_type == 'Trainer':
        st.subheader("Trainer Analysis")
        trainer = st.selectbox("Choose a trainer:", ['Kambale madam','Mrinalini','Shital vidhate','Sacnin sir','Rani Panchal'])
        trainer_data = data[data['name of instructor'] == trainer]
        if not trainer_data.empty:
            generate_trainer_plotsM(trainer_data)
        else:
            st.write("No data available for the selected trainer.")

