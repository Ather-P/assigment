import pandas as pd
import numpy as np
import streamlit as st
import pickle
from pycaret.classification import load_model, predict_model
from datetime import *

def get_model():
	return load_model("Prediction_model")

def predict(model,input_df):
	prediction = predict_model(model,data = input_df)
	return prediction['prediction_label'][0]

model = get_model()

st.title("Customers who prefer to book the vehicle using the website")
created_date = st.date_input('Created Date')
created_time = st.time_input('Created Time')
updated_date = st.date_input('Updated Date')
updated_time = st.time_input('Updated Time')
intro_view = st.sidebar.selectbox('Intro View',('yes','no'))
audio_journey = st.sidebar.selectbox('Audio Journey',('yes','no'))
self_explore = st.sidebar.selectbox('Self Explore',('yes','no'))
accessories = st.sidebar.selectbox('Accessories',('yes','no'))
emi = st.sidebar.selectbox('EMI',('yes','no'))
test_drive = st.sidebar.selectbox('Test Drive',('yes','no'))
model_id = st.sidebar.selectbox('Model ID',(1,2,3,4,5,6,7))
variant_id = st.sidebar.selectbox('Variant ID',(62,  85,  93,  80,  88,  67,  75,  65,  71,  86,  70,  44,  68,
        46,  47,  81,  73,  74,  59,  45,  50,  63,  83,  69,  82,  77,
        53,  57,  64,  56,  92,  87,  40,  94,  58,  36,  72,  60,  41,
        78,  89,  84,  76,  52,  90,  38,  55, 134, 133, 108, 136, 135))
showroom_price = st.number_input('Showroom Price')
accessories_price = st.number_input('Accessories price')
city = st.sidebar.selectbox('City',('Delhi', 'Calicut', 'Hyderabad', 'Surat', 'Pune', 'Nagpur',
       'Vizag', 'Chennai', 'Gurugram', 'Chandigarh', 'Mehsana',
       'Ahmedabad', 'Mumbai', 'Agra', 'Mohali', 'Bhubaneswar', 'Thane',
       'Gandhinagar', 'Madurai', 'Bengaluru', 'Raipur', 'Cochin',
       'Navi Mumbai', 'Ranchi', 'Kolhapur', 'Jabalpur', 'Bareilly',
       'Faridabad', 'Vadodara', 'Jaipur', 'Noida', 'Rajahmundry',
       'Sambalpur', 'Kanpur', 'Vijayawada', 'Aligarh', 'Jhansi',
       'Patiala', 'Nellore', 'Guwahati', 'Baramati', 'Vapi', 'Ajmer',
       'Hubli', 'Tirupati', 'Ghaziabad', 'Indore', 'Kottayam', 'Hasan',
       'Coimbatore', 'Kolkata', 'Roorkee', 'Patna', 'Dehradun',
       'Gandhidham', 'Trivandrum', 'Aurangabad', 'Puducherry',
       'Himmatnagar', 'Jalandhar', 'Nanded', 'Ludhiana', 'Guntur',
       'Amravati', 'Sonipat', 'Siliguri', 'Dhanbad', 'Mandi', 'Nashik',
       'Jodhpur', 'Latur', 'Warangal', 'Anand', 'Mangalore', 'Bharuch',
       'Gorakhpur', 'Hisar', 'Lucknow', 'Gulbarga', 'Thanjavur', 'Bhopal',
       'Bhatinda', 'Ambattur', 'Gwalior', 'Udaipur', 'Udupi', 'Goa',
       'Salem', 'Shimoga', 'Allahabad', 'Srinagar', 'Malappuram',
       'Varanasi', 'Ambawadi', 'Yamuna Nagar', 'Rajkot', 'Moradabad',
       'Sultanpur', 'Mysore', 'Angul', 'Dibrugarh', 'Prayagraj', 'Rohtak',
       'Jammu', 'Ambala', 'Chandrapur', 'Haldwani'))
state = st.sidebar.selectbox('State',('Delhi', 'Kerala', 'Telangana', 'Gujarat', 'Maharashtra',
       'Andhra Pradesh', 'Tamil Nadu', 'Haryana', 'Chandigarh',
       'Uttar Pradesh', 'Punjab', 'Odisha', 'Karnataka', 'Chhattisgarh',
       'Jharkhand', 'Madhya Pradesh', 'Rajasthan', 'Assam', 'West Bengal',
       'Uttarakhand', 'Bihar', 'Himachal Pradesh', 'Goa',
       'Jammu and Kashmir'))
pincode = st.number_input('Pincode', min_value=100000, max_value=999999)

combined_created = datetime.combine(created_date,created_time)
combined_updated = datetime.combine(updated_date,updated_time)
input_dic = {'Created At':combined_created,'Updated At':combined_updated,'Intro View':intro_view,'Audio Journey':audio_journey,'Self Explore':self_explore,
	     'Accessories':accessories,'EMI':emi,'Test Drive':test_drive,'Model ID':model_id,'Variant ID':variant_id,'Showroom Price':showroom_price,
		 'Accessories price':accessories_price,'City':city,'State':state}
input_df = pd.DataFrame([input_dic])

if st.button("Predict"):
	output = predict(model,input_df)
	st.text("Prediction done")
	
	if output== 'yes':
		st.success('Customer will book through Website')
	else:
		st.success('Customer will not book')