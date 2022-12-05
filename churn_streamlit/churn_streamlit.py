import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title='ABC Bank',
                   page_icon='💰', layout='wide')
st.title('Churn prediction 🚶‍♀️- ABC Bank')


def model_predict(coln):
    with coln:
        # Data processing
        # drop surname and row number and exited
        ip_data = {'CreditScore': credit_score_val, 'Geography': geography_val,
                   'Gender': gender_val, 'Age': age_val, 'Tenure': tenure_val,
                   'Balance': float(balance_val), 'NumOfProducts': product_val, 'HasCrCard': cc_val,
                   'IsActiveMember': active_mem_val, 'EstimatedSalary': estimated_sal_val}

        # convert input into DF
        ip_df = pd.DataFrame(ip_data, index=[0])

        # get original dataset and drop unnecessary
        org_csv_path = "D:\project\ML_daddy_staging\Bank_churn\Bank_churn_data\churn.csv"
        original_df = pd.read_csv(org_csv_path)

        coriginal_df = original_df.drop(
            ['CustomerId', 'Surname', 'RowNumber', 'Exited'], axis=1)

        ip_df = pd.concat([ip_df, coriginal_df], axis=0)

        ip_df = pd.get_dummies(ip_df, columns=["Geography", "Gender"])

        labelencoder = LabelEncoder()
        ip_df['IsActiveMember'] = ip_df['IsActiveMember'].map(
            {'Yes': 1, 'No': 0})
        ip_df['HasCrCard'] = ip_df['HasCrCard'].map({'Yes': 1, 'No': 0})

        # we will take only the user input i.e the 1st row
        ip_df = ip_df.head(1)
        st.write('Input provided')
        st.write(ip_df)

        # model predict
        saved_model_path = "D:\project\ML_daddy_staging\Bank_churn\churn_random_for_clf_model.pkl"
        loaded_model = pickle.load(open(saved_model_path, 'rb'))

        # Predicting the output
        # getting probability of each class
        pred_prob = loaded_model.predict_proba(ip_df)

        st.write('Prediction🕵️')
        pred_df = pd.DataFrame(pred_prob, columns=[
            'Chance of Customer Leaving', 'Chance of Customer Staying'])
        st.write(pred_df)


_, _, centre, _, _ = st.columns(5)
with centre:
    st.write("Enter the customer details")
c1, _ = st.columns([2, 1])
with c1:
    customer_id_val = st.number_input('Customer ID')
c1, c2, c3 = st.columns(3)
with c1:
    credit_score_val = st.number_input('Credit score')
    geography_val = st.selectbox(
        'Location', options=['France', 'Germany', 'Spain'])
    gender_val = st.radio(
        'Gender', options=['Male', 'Female'], horizontal=True)
    balance_val = st.number_input('Balance')
    tenure_val = st.number_input('Tenure period')

with c2:
    product_val = st.number_input('Num of product')
    # age min 10 since 10 and above is req to have your own bank a/c
    age_val = st.selectbox('Age', options=np.arange(start=10, stop=100))
    cc_val = st.radio('Has Credit Card?', options=[
                      'Yes', 'No'], horizontal=True)
    estimated_sal_val = st.number_input('Est.Salary')
    active_mem_val = st.radio('Active customer?', options=['Yes', 'No'])

model_predict(c3)
