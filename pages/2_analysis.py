import streamlit as st
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import ast
import re
import pandas as pd
import seaborn as sns

df = pd.read_csv('datasets/gurgaon_properties_missing_value_imputation.csv')
def extract_features(feature_string):
    """Convert messy list-string into a flat list of features"""
    # Extract all the [] blocks
    parts = re.findall(r"\[.*?\]", feature_string)

    # Convert each block into a real Python list
    lists = [ast.literal_eval(p) for p in parts]

    # Flatten
    all_features = [item for sublist in lists for item in sublist]

    return all_features


feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))
st.set_page_config('Plotting')

st.title('Analytics')

import pandas as pd

new_df = pd.read_csv('datasets/data_viz1.csv')

group_df = new_df.groupby('sector').mean(['price_per_sqft'])[['price', 'price_per_sqft', 'built_up_area', 'lat', 'long']]

st.subheader('Price Per Sector in Gurgaon')
fig = px.scatter_map(group_df, lat="lat", lon="long",color="price_per_sqft", size="built_up_area",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, hover_name=group_df.index)
st.plotly_chart(fig, use_container_width=True)

# wordcloud for all gurgaon real estate
st.subheader('Wordcloud for Amnities provided in Gurgaon')
wordcloud = WordCloud(width=600, height=600, background_color='white', stopwords={'s'},
                      min_font_size=10).generate(feature_text)

fig2, ax2 = plt.subplots(figsize=(3, 3))
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis('off')
st.pyplot(fig2, use_container_width=False)

# wordcloud for sector based real estate
st.subheader('Amnities per Sector')
wc_group_df = pd.read_csv('datasets/wc_df.csv')
sector_names = wc_group_df['sector'].unique().tolist()

select_sector = st.selectbox('Sector', sector_names)

# st.dataframe(wc_group_df)
wc_group_df.set_index('sector', inplace=True)
feature_list = extract_features(wc_group_df.loc[select_sector, :].values[0])
feature_string = ' '.join(feature_list)
wc = WordCloud(width=600, height=600, background_color='white', stopwords={'s'},
                          min_font_size=10).generate(feature_string)

fig1, ax1 = plt.subplots(figsize=(3, 3))
ax1.imshow(wc, interpolation='bilinear')
ax1.axis('off')
st.pyplot(fig1, use_container_width=False)

# scatter plot for price vs area

st.subheader('Price vs Area Scatterplot')
property_type = st.selectbox('Property Type', ['flat', 'house'])

if property_type == 'flat':
    fig3 = px.scatter(df[df['property_type']== 'flat'], x='built_up_area', y='price', color='bedRoom', title='Area vs Price')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.scatter(df[df['property_type'] == 'house'], x='built_up_area', y='price', color='bedRoom',
                      title='Area vs Price')
    st.plotly_chart(fig3, use_container_width=True)


# pie chart for bhk
sector_list = df['sector'].unique().tolist()
overall = ['Overall']
sector_list = overall + sector_list
sector_room = st.selectbox('Sector', sector_list)
st.subheader('Bedrooms distribution')

if sector_room == 'Overall':
    fig4 = px.pie(df, names='bedRoom', color='bedRoom', title='Bedrooms percentage')
    st.plotly_chart(fig4, use_container_width=True)
else:
    fig4 = px.pie(df[df['sector'] == sector_room], names='bedRoom', color='bedRoom', title='Bedrooms percentage')
    st.plotly_chart(fig4, use_container_width=True)

# seaborn for distplot
st.subheader('Distplot for flats and houses')
fig5 = plt.figure(figsize=(10,4))
sns.distplot(df[df['property_type'] == 'house']['price'], label='price')
sns.distplot(df[df['property_type'] == 'flat']['price'], label='price')
st.pyplot(fig5)