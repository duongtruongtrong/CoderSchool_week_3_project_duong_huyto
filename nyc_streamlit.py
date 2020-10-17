import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

import streamlit as st
from PIL import Image

airbnb_image = Image.open('airbnb-678x381.jpg')
st.image(airbnb_image, use_column_width = True)

# Outline:
# 1. Airbnb instroduction
# 2. Big question
# 3. COVID - Why still airbnb?
#     Unique places with unique experience;
#     Time to relax a bit, but still follow COVID rules.
# 4. How to choose an airbnb:
#     Price ranges;
#     Accommodate types;
#     Locations;
#     Unique experience;
#     Cleanliness;
#     Safety: Crime Rate, COVID Rate.
# 5. Result: A short list of "unique" airbnb to choose
# 6. Project difficulty

st.header('Airbnb Introduction:')
st.write('- Airbnb, the world leader in accommodations of the “sharing economy”, allows you to find places to stay directly from individuals in thousands of cities around the world.')
st.write('- It allows you to rent apartments (or even entire houses) from people all over the world, almost everywhere in fact. The platform really revolutionized the world of accommodations.')

<<<<<<< HEAD

=======
covid_image = Image.open('covid.jpg')
st.image(covid_image, use_column_width = True)
>>>>>>> 3c7d4a5ff33c0e6ad7c7695d3d073711602b5f93
st.header('Covid - Why choose an Airbnb?')

st.write('We are restricted to travel ever since the pandemic started. Therefore, the best option we have is to travel around the our area')
st.write('So why choose an Airbnb?')

st.markdown('**Live As a Local**')
st.write('- Airbnb provides you the unique experience that hotels cannot.')
st.write('- Airbnb allows you to live more like a local than a tourist.')
st.write('- Airbnb usually does a better job of immersing you in the local culture than getting a hotel room')


st.markdown('**Meet People**')
st.write('- Airbnb gives you the option to stay with the host. The host will often be happy to welcome you and to tell you every interesting thing about the place you visit.')

st.markdown('**Save Money(sometimes)**')
st.write('- Depends on the location, Airbnbs are usually cheaper than hotels')
st.write('- Especially when you travel in a group, retinting an Airbnb is definitely cheaper than a hotel')

st.markdown('**Unique Experience**')
st.write('- Some Airbnbs blah blah')

st.header('How To choose an Airbnb?')
