import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Price Predictor')

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as f:
    pipe = pickle.load(f)

st.header('Enter your inputs')

# property type
property_type = st.selectbox('Property Type', ['flat', 'house'])

# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# bedroom
bedrooms = float(st.selectbox('No. of Bedrooms', sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathroom = float(st.selectbox('No. of Bathrooms', sorted(df['bathroom'].unique().tolist())))

# balcony
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

# property age
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

# Built up area
built_up_area = float(st.number_input('Built Up Area'))

# servant room
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))

# store room
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

# furnishing type
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# luxury category
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

# floor category
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.text(np.expm1(pipe.predict(one_df)))