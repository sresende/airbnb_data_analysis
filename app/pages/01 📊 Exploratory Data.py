import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns
import pydeck as pdk
from urllib.error import URLError

listing = pd.read_csv('../data/listing_eda.csv')

st.set_page_config(page_title="Exploratory Data", page_icon="🌍")
st.markdown("## Plotting Data")
st.write(
    """Here you can explore and display some plots from listing data."""
)
#QUARTILE
Q1 = listing['price'].quantile(0.25)
Q3 = listing['price'].quantile(0.75)
IQR = Q3 - Q1
listing.drop(listing[listing['price'] < (Q1 - 1.5 * IQR)].index, inplace=True)   
listing.drop(listing[listing['price'] > (Q3 + 1.5 * IQR)].index, inplace=True)

## BarChart
groupby_type = st.selectbox(
    'Barcharts for Average Price Accomodations',
    ('neighbourhood_group_cleansed','room_type'))
st.bar_chart(listing.groupby(by=groupby_type).mean()['price'] )

#### histogram data
st.write("Price Histograms by Room Type")
# Add histogram data
x1 = listing[listing['room_type']== 'Entire home/apt']['price']- 2
x2 = listing[listing['room_type']== 'Private room']['price']
x3 = listing[listing['room_type']== 'Shared room']['price'] + 2
x4 = listing[listing['room_type']== 'Hotel room']['price'] + 4

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[5, 7.25, 10, 12.5])
# Plot!
st.plotly_chart(fig, use_container_width=True)

## Histogram
hist_type = st.selectbox(
    'Distribution Accomodations',
    ('price','neigh_price_sqft'))

arr = listing[hist_type]
fig, ax = plt.subplots()
plt.figure(figsize = (12, 6))
ax.hist(arr, bins=100)
ax.set_title(f'Distribution per {hist_type}')
ax.set_xlabel("Price")
ax.set_ylabel("Counts")
st.pyplot(fig)



## Scatter Plot ##
import altair as alt
room_type = st.selectbox(
    'Scatter Plots by Acommodation Type and Neighborhood',
    ('Entire home/apt','Private room','Shared room','Hotel room'))
df_room_type = listing[listing['room_type']==room_type]

plt.figure(figsize=(25,8))

sns.set(style='whitegrid')
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 8))
ax = sns.scatterplot(x = df_room_type['neighbourhood_cleansed'],
                    y="price",
                    data=df_room_type,
                    hue="room_type", s=20
                    );
ax.tick_params(axis='x', rotation=90)
plt.title("Entire Place Listings per Neighborhoods and Prices ")
plt.xlabel("Neighborhoods")
plt.ylabel("Prices");
st.pyplot(fig)
#st.sidebar.header("Plotting Data")

