import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
#import folium
import numpy as np
import pydeck as pdk
#from streamlit_folium import folium_static

# Reading dataset
listing = pd.read_csv('../data/listing_eda.csv')

st.set_page_config(page_title="New York City Airbnb Listings", page_icon="🌍")

st.markdown("## New York City Airbnb Listings")
st.sidebar.header("New York City")
st.write(
    """This map of New York City shows accommodations for each Neighborhood selected at the sidebar
and display it as geospatial data by price."""
)
st.sidebar.markdown("### Mapping Listings")
neighbourhood_cleansed = st.sidebar.selectbox(
    'Select Neighborhood:',
('bedford-stuyvesant','williamsburg','bushwick','upper west side','crown heights',"hell's kitchen",
 'upper east side','east village','east harlem','astoria','lower east side','greenpoint',
 'chelsea','washington heights','east flatbush','flatbush','flushing','long island city',
 'west village','clinton hill','east new york','jamaica','woodside','sunset park','financial district',
 'fort greene','park slope','sunnyside',
 'ridgewood','kips bay','canarsie','elmhurst','prospect heights','jackson heights','chinatown',
 'wakefield','murray hill','inwood','soho','nolita','carroll gardens','rosedale', 'greenwich village',
 'gowanus','bay ridge','sheepshead bay','richmond hill','forest hills','st. albans','kensington',
 'windsor terrace','boerum hill','theater district','queens village','brownsville','maspeth',
 'tribeca','woodhaven','midwood','flatlands','mott haven','ozone park','rockaway beach',
 'borough park','corona','rego park','brooklyn heights','kingsbridge','williamsbridge','little italy','bensonhurst',
 'gravesend','cobble hill','concourse','red hook','bayside','glendale','allerton',
 'parkchester','brighton beach','kew gardens','st. george','roosevelt island','battery park city',
 'far rockaway','flatiron district','two bridges','central park','clason point','tompkinsville',
 'fort hamilton','concourse village','downtown brooklyn','middle village','mount hope','briarwood',
 'jamaica estates','edenwald','noho','throgs neck','howard beach','fresh meadows','pelham gardens',
 'kew gardens hills','van nest',
 'bath beach', 'morris park','eastchester','belmont','mariners harbor','west brighton','hollis',
 'vinegar hill','morris heights','civic center','coney island','highbridge','stapleton','dyker heights',
 'port richmond','norwood','dumbo','marine park',
 'melrose','university heights','unionport','grant city','city island','midland beach','jamaica hills',
 'clifton','new brighton','grymes hill','pelham bay','oakwood','new dorp beach','prospect park',"prince's bay",
 'rosebank','riverdale','great kills','dongan hills','arden heights','castleton corners','bay terrace',
 'west farms','todt hill','tottenville','new springville','eltingville','south beach','castle hill',
 'westerleigh',
 'woodrow'))

## Plotting Map
listing_locations = listing[['latitude', 'longitude', 'price','neighbourhood_cleansed']]
listing_locations = listing[listing_locations['neighbourhood_cleansed']==neighbourhood_cleansed]

#df = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])
df =listing_locations
#st.map(df)
#map = folium.Map(location=[listing_locations.latitude.mean(), listing_locations.longitude.mean()], zoom_start=14, control_scale=True)
#for index, location_info in listing_locations.iterrows():
#    folium.Marker(location = [location_info['latitude'], location_info['longitude']], popup = str(location_info['price'])).add_to(map)



st.pydeck_chart(
    pdk.Deck(
     initial_view_state=pdk.ViewState(
         latitude=listing_locations.latitude.mean(),
         longitude=listing_locations.longitude.mean(),
         zoom=11,
         pitch=30,),
     layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[longitude, latitude]',
            radius=50,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[longitude, latitude]',
             get_radiusc=200),
        ],
    )
)

st.map(df, zoom=12)


#import leafmap.foliumap as leafmap
#st.dataframe(df)
#m = leafmap.Map(center=(-31.416668, -64.183334), zoom=5)
#m.add_circle_markers_from_xy(df, x="longitude", y="latitude")
#m.Popup()