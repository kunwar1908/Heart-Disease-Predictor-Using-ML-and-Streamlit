import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Heart disease Prediction App

This app predicts If a patient has a heart disease

""")

st.sidebar.header('User Input Features')



# Collects user input features into dataframe

def user_input_features():
    age = st.sidebar.number_input('Enter your age: ')
    sex  = st.sidebar.selectbox('Sex (1 = male; 0 = female)',(0,1))
    cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
    tres = st.sidebar.number_input('Resting blood pressure: ')
    chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)',(0,1))
    res = st.sidebar.number_input('Resting electrocardiographic results: ')
    tha = st.sidebar.number_input('Maximum heart rate achieved: ')
    exa = st.sidebar.selectbox('Exercise Induced Angina (1 = yes; 0 = no)',(0,1))
    old = st.sidebar.number_input('ST Depression: ')
    slope = st.sidebar.number_input('Slope of the Peak Exercise ST Segment')
    ca = st.sidebar.selectbox('Number of major vessels',(0,1,2,3))
    thal = st.sidebar.selectbox('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect):',(0,1,2))

    data = {'age': age,
            'sex': sex, 
            'cp': cp,
            'trestbps':tres,
            'chol': chol,
            'fbs': fbs,
            'restecg': res,
            'thalach':tha,
            'exang':exa,
            'oldpeak':old,
            'slope':slope,
            'ca':ca,
            'thal':thal
                }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

# Combines user input features with entire dataset
# This will be useful for the encoding phase
heart_dataset = pd.read_csv('C:/Users/kunwa/Python/Projects/Heart-Disease-prediction-ML-and-Streamlit-main/heart.csv')
heart_dataset = heart_dataset.drop(columns=['target'])

df = pd.concat([input_df,heart_dataset],axis=0)

# Encoding of ordinal features
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
df = pd.get_dummies(df, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])

df = df[:1] # Selects only the first row (the user input data)

st.write(input_df)
# Reads in saved classification model
load_clf = pickle.load(open('C:/Users/kunwa/Python/Projects/Heart-Disease-prediction-ML-and-Streamlit-main/Random_forest_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df.values)
prediction_proba = load_clf.predict_proba(df.values)


st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)