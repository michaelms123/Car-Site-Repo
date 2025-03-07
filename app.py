import pandas as pd
import plotly_express as px 
import streamlit as st

vehicles_df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
vehicles_df['manufacturer'] = vehicles_df['model'].apply(lambda x: x.split()[0])
vehicles_df.

st.header('Data Viewer')
st.dataframe(vehicles_df)

#Histogram for vehicle types by manufacturer
st.header('Vehicle Types by Manufacturer')
fig = px.histogram(vehicles_df, x='manufacturer', color='type')
st.write(fig)


#Histogram of condition vs model year
st.header('Histogram of Condition vs. Model Year')
fig_2 = px.histogram(vehicles_df, x='model_year', color='condition')
st.write(fig_2)

st.header('Compare Price Distribution Between Manufacturers')
#Get a list of car manufacturers 
manufac_list = sorted(vehicles_df['manufacturer'].unique())
#Get user's inputs from dropdown menu
manufacturer_1 = st.selectbox(label='Select Manufacturer 1', options=manufac_list, index=manufac_list.index('chevrolet'))
#Repeat for 2nd dropdown menu
manufacturer_2 = st.selectbox(label='Select Manufacturer 2', options=manufac_list, index=manufac_list.index('hyundai'))
#Filter for the df 
mask_filter = (vehicles_df['manufacturer'] == manufacturer_1) | (vehicles_df['manufacturer'] == manufacturer_2)
filtered_df = vehicles_df[mask_filter]

#Added checkbox if a user wants to normalise the histogram 
normalise = st.checkbox('Normalise Histogram', value=True)
if normalise:
    histnorm = 'percent'
else: 
    histnorm = None 

#Creating the histogram 
fig_3 = px.histogram(filtered_df, x='price', nbins=30, color='manufacturer', histnorm=histnorm, barmode='overlay')
#displaying the figure 
st.write(fig_3)
