import streamlit as st
from PIL import Image
import numpy as np
import pickle
import time
#
import json
#import torch
from collections import Counter
image = Image.open('misinformation.png')
st.image(image, caption='Combatting online misinformation')

st.header("Hi there -- are you wondering if an online post/headline is credible? Airton developed this web app to guide you.")
st.subheader("Paste the text or headline below and we'll make a prediction by comparing any given headline or text to thousands of other social media posts.")
#st.subheader("If the model classifies the given headline or post as something that would be observable in a credible news media post, it is likely trustworthy and will assign a percentage likelihood with its prediction, otherwise it'll  classify the text as 'conspiracy' and assign a similar probability.")

with open("subreddit.pkl", "rb") as f:
    classifier = pickle.load(f)

headline = [st.text_input('Enter the post text or headline here')]
def fakeorreal(headline, gs):
    headline = gs.best_estimator_.named_steps['countvectorizer'].transform(headline).reshape(1, -1)
    prediction = gs.best_estimator_.named_steps['multinomialnb'].predict(headline)
    if st.button('Generate Prediction'):
        generated_pred = prediction = gs.best_estimator_.named_steps['multinomialnb'].predict(headline)
        probability = gs.best_estimator_.named_steps['multinomialnb'].predict_proba(headline).max()
        if generated_pred[0] == 'worldnews':
            st.write(f"There is a {round(probability, 2)*100} percent chance that this text/headline is credible, but please continue to follow healthy digital media consumption practices")
            st.balloons()
        else:
            st.write(f"There is a {round(probability, 2)*100} percent chance that this text/headline is not credible, please don't spread without double checking")
            


fakeorreal(headline, classifier)


