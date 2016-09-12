# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret'],
    token=os.environ['token'] ,
    token_secret=os.environ['token_secret'] 
)

client = Client(auth)

params = {
    'term': 'food',
    'lang': 'en'
}


def yelp_search(address):
    response = client.search(address, **params) 
    top3_recommendations ={response.businesses[0].name:response.businesses[0].location.address[0] + " " + response.businesses[0].location.postal_code + " " + response.businesses[0].location.city, response.businesses[1].name:response.businesses[1].location.address[0] + " " + response.businesses[1].location.postal_code + " " + response.businesses[1].location.city, response.businesses[2].name:response.businesses[2].location.address[0] + " " + response.businesses[2].location.postal_code + " " + response.businesses[1].location.city  }
    return top3_recommendations

#print(response.businesses[0].name)
#print(response.businesses[0].location.address)

#print(response.businesses[1].name)
#print(response.businesses[1].location.address)

#print(response.businesses[2].name)
#print(response.businesses[3].location.address)

#response = client.search('Madrid, Spain', **params) 
#top3_recommendations ={response.businesses[0].name:response.businesses[0].location.address[0] + " " + response.businesses[0].location.postal_code + " " + response.businesses[0].location.city, response.businesses[1].name:response.businesses[1].location.address[0] + " " + response.businesses[1].location.postal_code + " " + response.businesses[1].location.city, response.businesses[2].name:response.businesses[2].location.address[0] + " " + response.businesses[2].location.postal_code + " " + response.businesses[1].location.city  }
#print(top3_recommendations)
