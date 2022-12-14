# Prediction Model for Airbnb's Acommodations Price
Data Analysis and Machine Learning on Airbnb Dataset

## Problem Statement
-----
The main purpose of this project is to develop a machine learning model that can predict prices for accommodations there to be listed on the Airbnb website.  Here we consider two types of audience, the main one being Airbnb interested in providing the user with a price suggestion during the listing process based on its main features such as type of accommodation, number of rooms and neighborhood. The secondary stakeholders would be people who are interested in using the Airbnb service by making their properties available for rent on their website and having an idea of how much this service could earn from it.


![](/images/map_nyc.png)


Several supervised and unsupervised machine learning models were developed considering the different characteristics of the dataset, pre-processing data, tunning tecniques and than evaluated according to their score and average error sum (RMSE) metrics.


Once the final model was selected, an App was developed to predict housing prices using the Streamlit library. This App, in addition to providing the price prediction model, provides an interface to interact with Airbnb data, making it possible to perform an exploratory analysis of the dataset by defining some parameters.

## Datasets 
----
Two data sets were used in this project. The first 'Listings.csv' with 39,881 rows and 75 columns was acquired through the Airbnb data explorer website [1] and contains information related to all accommodations listed on the website for the quarterly data for the last 12 months (Oct 2021 - Sept 2022). Another dataset was also used to add value to the modeling of our model - Neighborhood_price.csv - and was acquired in the data dashboard of the Street Easy website, which contains information regarding the real estate market in New York City and contains square foot prices for rentals in major its neighborhoods.

List of datasets:
* [`Listing.csv`](http://data.insideairbnb.com/united-states/ny/new-york-city/2022-09-07/data/listings.csv.gz) | [Dictionary](/data/dictionary.txt)
* [`Neighborhood_price.csv`](http://data.insideairbnb.com/united-states/ny/new-york-city/2022-09-07/data/listings.csv.gz) | [Dictionary](/data/dictionary_price.txt)

After cleaning the data, applying features engineering and input strategies we got a final dataset of size 23645 x 23 to training our machine learning models. 

We remove the outliers and started our analysis by looking at how the distribution of price listings behaves in the histogram chart and we could observe that the data is skewed to the right. 

![](/images/histogram_prices.png)

When this happens, it is common to apply a logarithmic transformation to the target (price) in an attempt to correct it. In our specific case, we applied this transformation and achieved a slight increase in test and training scores in most of our models.

If we look at the correlation between the characteristics of the dataset, we can observe that the variables 'accommodations', 'bedrooms', 'beds', 'bathrooms_nbr', 'neigh_price_sqft' have a higher correlation among the 23 characteristics found in the dataset but the first three ('bedrooms', 'beds') are very related to each other (multicolinearity).

![](images/corr.png)

 Longitude and latitude also have a relatively strong relationship with price, however we can understand that this information is already 'included' in the category variable neighborhood. 
 
 The boxplot below shows the 10 highest priced neighborhoods in NYC and the neighborhood group they're belong to.

![](images/boxplot_top10_neigbohood2.png) 

## Machine Learning Models Evaluation
-----
The dataset with 23 columns in total was scaled and hot encoded before being used to training our models. We started our model evaluation checking the baseline model and getting its score which has a negative value of -0.0001 meaning that the model is pretty bad at predictions. 

At first, we implemented a linear regression model and got a score of 0.64932 on the training set and -4.4354 on the test set. A Linear Regression model can be a good choice in a regression problem because its coefficintes can be used  to  interpret or to do inference at the target variable if the LINE assumptions be met. In this particular case, the LINE assumptions were not met so we couldn't use its coefficients to inference. Following, we applied lasso and ridge reguralization to see if it can improve its performance and we got the scored for Lasso 0.6361(Train), 0.6272 (Test) and 144.961 (RMSE). The scores for Ridge were 0.6401 (Train), 0.6295 (Test) and 144.774 (RMSE).

Then the following models were implemented: K-Nearest Neighbors Regression, Decision Tree Regressor, RainForest Regressor, Recurrent Neural Network associated with gridsearch and stacking techniques. 

Below is the benchmark table with the three models that had the best score among them.

![](images/models_benchmark.png)

The Rain Forest model had the scores 0.8866 (Train), 0.6818 (Test) and 150.465(RMSE) and we chose this one as the best model because it had the higher score on the Test set and not that bad value at RSME. This model was also the one selected to be used in the Streamlit app to predict the prices simulation. The code for the app can be found at the app folder in this same repository.



Later, in a second attempt to build better models, we try to apply transfer learning using clusters. so we create a new column 'cluster' using KMeans() to replace the column 'neighborhoods' and see if the  performance models increase. For this, a search for best value of k  was performed and returned the k value equals 150 - according to the silhouette value.

![](images/output_cluster.png)



## Conclusions and Recommendations
---

We could get at two conclusions for this project: first one, the feature engineering 'amenities_count' and 'description_listing_count' didn't increased the performance on our models and, the second one,  play around latitude/longitude or cluster with transfer learning to replace the neighborhood didn't also work.

Another conclusion after analyzing the data, it's that some variables are more important than others in determining the accommodation' prices, for example, the neighboord feature carries more weight to the target than the number of beds or baths.

As a suggestion, after these conclusions,  it is consider that if you want to add value to accomodation it will be more efficient increase the capacity of accommodate people than necessarily adding a room for it.
.

---
**References**: \
[1] [*Airbnb Get the Data Site*](http://data.insideairbnb.com/united-states/ny/new-york-city/2022-09-07/data/listings.csv.gz) \
[2] [*StreetEasy NYC Prices Data Dashboard*](https://streeteasy.com/blog/data-dashboard/)