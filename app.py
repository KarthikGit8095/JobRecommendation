import pandas as pd
import streamlit as st
import pickle

def recommend(job):
    job_index = jobs[jobs['Title'] == job].index[0]
    distances = similarity[job_index]
    job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_jobs=[]
    for i in job_list:
        recommended_jobs.append(jobs.iloc[i[0]].Title)
    return recommended_jobs

jobs_dict= pickle.load(open('jobs_dict.pkl','rb'))
jobs= pd.DataFrame(jobs_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

st.image('dataset-cover.png')

st.title('JOB RECOMMENDER SYSTEM')
st.text("")
selected_job_name= st.selectbox(
    'Search',
    jobs['Title'].values)
st.text("")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button('Recommend'):
        recommendation = recommend(selected_job_name)
        for i in recommendation:
            st.write(i)


