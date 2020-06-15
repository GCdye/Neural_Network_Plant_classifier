import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
st.title("Iris App")  # h1
st.header("Our ML project")  # h2
st.subheader("By: My team")  # h3
df_iris = px.data.iris()
df_iris
X = df_iris.drop(columns=["species", "species_id"])
y = df_iris["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)
lr = LogisticRegression()
lr.fit(X_train, y_train)
# get the 4 values we need from the user
# make them integers
s_w = int(st.text_input("Input the Sepal Width", 1))
s_l = int(st.text_input("Input the Sepal Length", 1))
p_w = int(st.text_input("Input the Petal Width", 1))
p_l = int(st.text_input("Input the Petal Length", 1))
user_input = np.array([s_w, s_l, p_w, p_l])
@st.cache
def score_obs(model, observation):
    """
    predicts the user's iris type
    Args:
        model (sklearn model object): already fit model
        observation (ndarray): the 4 measurements
    Returns:
        prediction (str): predicted type of iris
    """
    return model.predict(observation.reshape(1,-1))
prediction = score_obs(lr, user_input)
prediction

x = st.slider('x')
st.write(x, 'squared is', x * x)

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()
