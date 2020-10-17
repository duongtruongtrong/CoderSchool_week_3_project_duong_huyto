import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Setting the style 'seaborn' for your charts
plt.style.use('seaborn')

import warnings
warnings.filterwarnings('ignore')

import streamlit as st
from PIL import Image

# Outline:
# 1. Big question
# 2. Airbnb instroduction
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

# =========================================================================
# Begin

# Cache functions

@st.cache(allow_output_mutation=True)
def load_data(path):
    try:
        data = pd.read_excel(path)
    except:
        data = pd.read_csv(path)
    return data

# 1. Big question
st.title('Staycation with Airbnb')

# 2. Airbnb instroduction
airbnb_image = Image.open('airbnb-678x381.jpg')
st.image(airbnb_image, use_column_width = True)

st.header('1. Airbnb Introduction')

st.markdown('- **The world leader** in accommodations of the “sharing economy”, allows you to find places to stay directly from individuals in thousands of cities around the world.')

st.markdown('- Able to **rent apartments or even entire houses** from people all over the world, almost everywhere in fact.')

# 2. COVID - Why still airbnb?
st.header('2. COVID - Why choose an Airbnb?')
covid_image = Image.open('covid.jpg')
st.image(covid_image, use_column_width = True)

st.write('We are **restricted to travel** ever since the pandemic started. Therefore, the **best option** we have is to travel **around our area**.')

# NYC_Covid_Daily_CSV
nyc_covid_daily_oct_2020 = load_data('nyc_covid_daily_oct_2020.csv')
nyc_covid_daily_oct_2020['DATE_OF_INTEREST'] = pd.to_datetime(nyc_covid_daily_oct_2020['DATE_OF_INTEREST'])

# NYC_Covid_Daily_Chart

plt.rc('font', size=18) #controls default text size
plt.rc('axes', titlesize=22) #fontsize of the title
plt.rc('axes', labelsize=22) #fontsize of the x and y labels
plt.rc('xtick', labelsize=22) #fontsize of the x tick labels
plt.rc('ytick', labelsize=22) #fontsize of the y tick labels
plt.rc('legend', fontsize=22) #fontsize of the legend

covid, ax = plt.subplots(figsize=(18, 8))

covid.suptitle('New York COVID-19 Cases', fontsize=25)

sns.lineplot(x='DATE_OF_INTEREST', y='Cases', data=nyc_covid_daily_oct_2020, ax=ax, label='Daily')
sns.lineplot(x='DATE_OF_INTEREST', y='7-day average', data=nyc_covid_daily_oct_2020, ax=ax, label='7-day average')
ax.grid(True)

st.pyplot(covid)

st.subheader('You are a New Yorker')
st.markdown('- **Rarely** go to the other side of your city;')
st.markdown('- Or **visit other cities** in New York.')

st.subheader('Live As a Local with Unique Experience')
st.markdown('- **Unique experience** with Airbnb that hotels cannot provide.')
st.markdown('- **Immersing you in the local culture** than getting a hotel room')

st.subheader('Meet People')
st.markdown('Airbnb gives you the option to **stay with the local host**. The host will often be happy to welcome you and to tell you every interesting thing about the place you visit.')

st.subheader('Save Money')
st.markdown('_(sometimes)_')

st.markdown('- Airbnbs are usually **cheaper** than hotels _(depends on the location)_')
st.markdown('- **Travel in a group**, Airbnb is definitely cheaper than a hotel.')

# 4. How to choose an airbnb:
st.header('3. How To choose the best unique Airbnb?')

st.subheader('What is unique Airbnb?')
st.markdown('Airbnb with reviews **containing the word "unique"** and its synonyms: distinctive, special, extraordinary')

st.markdown('Example:')


st.markdown('Each Airbnb will have a certain number of "unique" reviews.')

# Airbnb total review distribution
df_meaningful_col = load_data('listings_meaningful_2020.xlsx')
plt.figure(figsize=(18,8))

ax = sns.boxplot(data=df_meaningful_col,
                 x='total_unique_reviews')
ax.set_xticks(list(range(0, 151, 2)))
ax.gird(True)