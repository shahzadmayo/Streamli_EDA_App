import imp
import streamlit as st
import seaborn as sns

st.header("This is the main body of the streamlit app")
st.text(" this is the second line of code ")
st.title("First streamlit app")

df= sns.load_dataset('iris')
st.write(df[['species','sepal_length','petal_length']].head(10))
st.bar_chart(df[['sepal_length','petal_length']])