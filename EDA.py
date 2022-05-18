import csv
from distutils.command.upload import upload
from doctest import Exmaple
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.markdown('''# ** Exploratory Data Analysis Web Application**
This App is developed by Shahzad Called **EDA APP**
''')

#how to upload file
with st.sidebar.header("Upload Your Dataset (.csv)"):
    uploaded_file=st.sidebar.file_uploader("Upload Your File",type=['csv'])

    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download)")

if uploaded_file is not None:
        @st.cache
        def load_csv():
         csv=pd.read_csv(uploaded_file)
         return csv
        df=load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profilng Report with Pandas**')
        st_profile_report(pr)
else:
     st.info('Awaiting for CSV file ')
if st.button('Press to use example data'): 
                @st.cache

                def load_data():
                    a = pd.DataFrame(np.random.rand(100, 5),
                    columns=['age','banana','codanics','Deutchland','Ear'])
                    
                    return a
  
                df = load_data()
                pr= ProfileReport(df, explorative=True)
                st.header('**Input DataFrame**')
                st.write(df)
                st.write('---')
                st.header('**Pandas Profiling Report**')
                st_profile_report(pr)


