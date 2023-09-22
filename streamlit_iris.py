import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import streamlit as st

df_iris = sns.load_dataset('iris')

st.subheader("Scatter plot 3D from Iris dataset")
df = df_iris.values

fig = px.scatter_3d(df_iris,
                 x="sepal_width",
                 y="sepal_length",
                 z="petal_length",
                 color="species",
                 color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
