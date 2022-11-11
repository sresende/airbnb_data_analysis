from operator import mod
import streamlit as st
import pickle

# @st.cache
def load_model():
  with open('../models/rf_model.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

model = load_model()

st.title('How much can you earn from Airbnb listing?')

st.subheader('Do you want you predict the price for your accomodation?')

txt = st.text_area('Write your host_is_superhost: ').strip()
txt_1 = st.text_area('Write your host_has_profile_pic').strip()
txt_2 = st.text_area('Write your host_identity_verified').strip()
txt_3 = st.text_area('Write your neighbourhood_cleansed').strip()
txt_4 = st.text_area('Write your room_type').strip()
txt_5 = st.text_area('Write your accommodates').strip()
txt_6 = st.text_area('Write your bedrooms').strip()
txt_7 = st.text_area('Write your minimum_nights').strip()
txt_8 = st.text_area('Write your maximum_nights').strip()
txt_9 = st.text_area('Write your number_of_reviews').strip()
txt_10 = st.text_area('Write your bathrooms_nbr').strip()
txt_11 = st.text_area('Write your neigh_price_sqft').strip()

if st.button('Submit'):
  if len(txt) > 0:
    pred = model.predict([txt])[0]
    probs = list(model.predict_proba([txt])[0])
    prob = probs[0] if pred == 'Edgar Allan Poe' else probs[1]
    st.write('You write like ', pred)
    st.metric('Probability', f'{100 * round(prob, 2)}%')
  else:
    st.write('Too pithy. Try writing something.')

# columns for my X_train
#       ['host_is_superhost', 'host_has_profile_pic', 'host_identity_verified',
#       'neighbourhood_cleansed', 'room_type', 'accommodates', 'bedrooms',
#       'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews',
#       'review_scores_rating', 'instant_bookable', 'bathrooms_type',
#       'bathrooms_nbr', 'neigh_price_sqft']

# Setting category columns to Dummify
# col_dummies = ['neighbourhood_cleansed', 'bathrooms_type', 'room_type']
# df = pd.get_dummies(df, prefix_sep="__", columns = col_dummies, drop_first = True);

