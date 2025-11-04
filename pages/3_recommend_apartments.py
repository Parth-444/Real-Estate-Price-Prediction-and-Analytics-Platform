import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Recommend Apartments')

cos_sim1 = pickle.load(open('datasets/cos_sim1.pkl', 'rb'))
final_sim = pickle.load(open('datasets/final_sim.pkl', 'rb'))
price_col_df = pickle.load(open('datasets/price_col_df.pkl', 'rb'))

def facilities_similarity(name):
    idx = price_col_df[price_col_df['PropertyName'] == name].index[0].tolist()
    sim_scores = list(enumerate(cos_sim1[idx]))
    sim_scores = sorted(sim_scores, key=lambda z: z[1], reverse=True)
    sim_scores = sim_scores[1:6]
    property_indices = [i[0] for i in sim_scores]
    recommendation_df = pd.DataFrame(
        {
            'Property_Name': price_col_df['PropertyName'].iloc[property_indices],
            'Similarity_Scores': sim_scores
        }
    )
    return recommendation_df

def final_similarity(name):
    idx = price_col_df[price_col_df['PropertyName'] == name].index[0].tolist()
    sim_scores = list(enumerate(final_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda z: z[1], reverse=True)
    sim_scores = sim_scores[1:6]
    property_indices = [i[0] for i in sim_scores]
    recommendation_df = pd.DataFrame(
        {
            'Property_Name': price_col_df['PropertyName'].iloc[property_indices],
            'Similarity_Scores': sim_scores
        }
    )
    return recommendation_df


st.title('Society Similar based on Facilities')
property_name = st.selectbox('Property Names', price_col_df['PropertyName'].values.tolist())

st.dataframe(facilities_similarity(property_name))


st.title('Society Similar based on Facilities and Price')
property_name1 = st.selectbox('Property Names ', price_col_df['PropertyName'].values.tolist())

st.dataframe(final_similarity(property_name1))