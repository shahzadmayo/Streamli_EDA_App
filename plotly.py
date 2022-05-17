from turtle import width
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Plotly and Streamlit App")
df= px.data.gapminder()
st.write(df)

st.write(df.describe())

#Data managment
year_option= df['year'].unique().tolist()
year= st.selectbox("which year shoud we plot?",year_option,0)
df=df[df['year']==year]

#ploting

fig= px.scatter( df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='continent',
log_x=True, size_max=55, range_x=[100,10000],range_y=[20,90],
animation_frame='year', animation_group='coountry')

fig.update_layout(width=800, height=600)
st.write(fig)