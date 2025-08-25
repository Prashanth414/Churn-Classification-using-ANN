import streamlit as st






# Streamlit app
st.title("Customer Churn Prediction")

# User inputs

#geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
#gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', min_value=18, max_value=100)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', min_value=0, max_value=10)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
