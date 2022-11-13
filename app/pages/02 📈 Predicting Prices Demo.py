from operator import mod
import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

# @st.cache
def load_model():
  with open('../models/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)
  return model

model = load_model()

st.title('Do you know how much your Airbnb accomodation can worth?')

st.subheader("Let's predict the price for it!")


host_is_superhost = st.radio(
    "Are you a Super Host?",
    ('Yes',  'No'))
if host_is_superhost == 'Yes':
    host_is_superhost = 1
else:
    host_is_superhost = 0

host_has_profile_pic = st.radio(
    "Do you pretend upload a picture for your Profile?",
    ('Yes',  'No'))
if host_has_profile_pic == 'Yes':
    host_has_profile_pic = 1
else:
    host_has_profile_pic = 0

host_identity_verified = st.radio(
    "Do you pretend to verify your identity?",
    ('Yes',  'No'))
if host_identity_verified == 'Yes':
    host_identity_verified = 1
else:
    host_identity_verified = 0

neighbourhood_cleansed = st.selectbox(
    'Select your neighborhood?',
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

room_type = st.selectbox(
    'Select your Acommodation Type?',
    ('Entire home/apt','Private room','Shared room','Hotel room'))
bedrooms = st.number_input('How many Bedrooms?')
accommodates = st.number_input('How many people it acommodates?')

minimum_nights = st.number_input('What is the minimum nights to stay?')
maximum_nights = st.number_input('What is the maximun nights to stay?')

##########################################
number_of_reviews = st.number_input('Insert the number of reviews')

##########################################
review_scores_rating = st.select_slider(
    'What is your review scores rating?',
    options=['1', '2', 
              '3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9',
              '4.0', '4.1','4.2','4.3','4.4','4.5','4.6','4.7', '4.8', '4.9', 
              '5'])
##########################################
instant_bookable = st.radio(
    "Is your accomodation instant Bookable",
    ('Yes',  'No'))
if instant_bookable == 'Yes':
    instant_bookable = 1
else:
    instant_bookable = 0
#########################################
bathrooms_type = st.selectbox(
    'Select your bathroom type?',
    ('private', 'shared'))
########################################
bathrooms_nbr = st.number_input('What is the number of bathrooms')
neigh_price_sqft = st.number_input('Insert the price per sqft for your neigboorhood')


       
datas_user = []

def get_user_input():
  data_user = {}
  data_user['host_is_superhost'] = host_is_superhost
  data_user['host_has_profile_pic'] = host_has_profile_pic
  data_user['host_identity_verified'] = host_identity_verified
  data_user['neighbourhood_cleansed'] = neighbourhood_cleansed
  data_user['room_type'] = room_type
  data_user['accommodates'] = accommodates
  data_user['bedrooms'] = bedrooms
  data_user['minimum_nights'] = minimum_nights
  data_user['maximum_nights'] = maximum_nights
  data_user['number_of_reviews'] = number_of_reviews
  data_user['review_scores_rating'] = review_scores_rating
  data_user['instant_bookable'] = instant_bookable
  data_user['bathrooms_type'] = bathrooms_type
  data_user['bathrooms_nbr'] = bathrooms_nbr
  data_user['neigh_price_sqft'] = neigh_price_sqft
  print("Tipo de do data_user", type(data_user))
  datas_user.append(data_user)
  return pd.DataFrame(datas_user)


def process_user_input(df):
  
  # Dummify
  col_dummies = ['neighbourhood_cleansed', 'bathrooms_type', 'room_type']   
  X_test = pd.get_dummies(df, prefix_sep="__", columns = col_dummies, drop_first = True);
  # Scalling
  sc = StandardScaler()
  return sc.transform(X_test)

if st.button('Submit'):
    
    df = get_user_input()
    print("retoronou", type(df))
    df_sc = process_user_input(df)
    

    #if len(user_inputs) > 0:
     # df_sc = process_user_input(inputs=user_inputs)
     # price = model.predict(df_sc)
      #probs = list(model.predict_proba([txt])[0])
      #prob = probs[0] if pred == 'Edgar Allan Poe' else probs[1]
      #st.write('The price for ypur accomodation is aproximatly: ', price)
      #st.metric('Probability', f'{100 * round(prob, 2)}%')
    #else:
      #st.write('Too pithy. Try writing something.')

# columns for my X_train
#       ['host_is_superhost', 'host_has_profile_pic', 'host_identity_verified',
#       'neighbourhood_cleansed', 'room_type', 'accommodates', 'bedrooms',
#       'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews',
#       'review_scores_rating', 'instant_bookable', 'bathrooms_type',
#       'bathrooms_nbr', 'neigh_price_sqft']

# Setting category columns to Dummify
# col_dummies = ['neighbourhood_cleansed', 'bathrooms_type', 'room_type']
# df = pd.get_dummies(df, prefix_sep="__", columns = col_dummies, drop_first = True);
