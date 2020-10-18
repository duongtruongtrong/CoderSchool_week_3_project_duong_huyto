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
# 0. Big question
# 1. Airbnb introduction
# 2. COVID - Why still airbnb?
#     Unique places with unique experience;
#     Time to relax a bit, but still follow COVID rules.
# 3. How to choose an airbnb:
#     Price ranges;
#     Accommodate types;
#     Locations;
#     Unique experience;
#     Cleanliness;
#     Safety: Crime Rate, COVID Rate.
# 4. Result: A short list of "unique" airbnb to choose
# 5. Project difficulty

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

# 0. Big question
st.title('Staycation with Airbnb')

# 1. Airbnb introduction
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

# Airbnb in COVID reasons
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

# 3. How to choose an airbnb:
st.header('3. How To choose the best unique Airbnb?')

# 3.1 Current number of airbnb listings in NYC: Chart and xlsx
df_meaningful_col_light = load_data('cleansed_listings_meaningful_2020_light.xlsx')

total_number_aribnb_nyc = len(df_meaningful_col_light)

total_number_aribnb, ax = plt.subplots(figsize=(2, 1))
total_number_aribnb.suptitle('Current number of Airbnb in New York', fontsize=15)
ax.text(x=0, y=0, s=str(total_number_aribnb_nyc), fontsize=40)
ax.axis("off")

st.pyplot(total_number_aribnb)

# 3.2 Unique Airbnb concept
st.subheader('What is unique Airbnb?')
st.markdown('Airbnb with reviews **containing the word "unique"** and its synonyms: distinctive, special, extraordinary.')

st.markdown('**Example**:')
df_sample_review = load_data('review_sample.xlsx')
st.dataframe(df_sample_review)

st.markdown('''**"Unique" Review of listing id 9576478**: Vitaliy provided very informative directions and instructions on getting into the apartment. The apartment was exactly like it was in the photos. Harlem is a **unique** neighbourhood in NYC and will give you a different flavour of the city.''')

st.markdown('''**"Unique" Review of listing id 27930717**: The location of this apartment is great - very close to the subway and it allows you to reach Manhattan quickly. Good restaurants in the neighborhood. Maxime's (Hidden by Airbnb) , who were at home when we stayed, were absolutely fantastic and they made our experience in NYC **special**.''')

# Airbnb total review distribution chart
st.subheader('Number of "unique" reviews.')

unique_review, ax = plt.subplots(figsize=(18, 5))
unique_review.suptitle('Number of "Unique" Reviews Distrubution', fontsize=25)

sns.boxplot(data=df_meaningful_col_light,
            x='total_unique_reviews',
            ax=ax)
ax.set_xticks(list(range(0, 8, 2)) + list(range(10, 161, 50)))

st.pyplot(unique_review)

st.markdown('Most of Aibnb has less than **2 "unique" reviews**, which is **too small**.')
st.markdown('The more "unique" reviews the Airbnb has, the more authentically unique the Airbnb is.')
st.markdown('The number of "unique" reviews should be more than the **whisker point** to be called a unique Aribnb.')

# Current number of airbnb listings in NYC: Chart and xlsx
df_unique_outliers = load_data('nyc_unique_aibnb.xlsx')

total_number_unique_aribnb, ax = plt.subplots(figsize=(2, 1))

total_number_unique_aribnb.suptitle('Total number of unique Airbnb in New York', fontsize=15)

ax.text(x=0, y=0, s=str(len(df_unique_outliers)), fontsize=40)

ax.axis("off")

st.pyplot(total_number_unique_aribnb)

# 3.2 Price Range with: Neighborhood and Room types
price_range, ax = plt.subplots(figsize=(20, 8))
price_range.suptitle("Price Ranges")
sns.boxplot(data=df_unique_outliers,
            x='price',
            ax=ax)
ax.set_xticks(list(range(0, 1500, 100)))
st.pyplot(price_range)

st.write('**0-300: Reasonable Price**')
st.write('**Over 300: Comming to Luxury**')

max_price = df_unique_outliers['price'].max()
min_price = df_unique_outliers['price'].min()


price_slider = st.slider("Choose a Price", round(int(min_price), -1),int(max_price), (30, 300), 10)

f, ax = plt.subplots(figsize=(20, 8))
f.suptitle("Price vs Neighborhood")
sns.histplot(data=df_unique_outliers,
            x='price',
            hue='neighbourhood_group_cleansed',
            ax=ax,
            multiple="stack",
            stat='count', bins=list(range(price_slider[0], price_slider[1], 50)))

ax.set_xticks(list(range(price_slider[0], price_slider[1], 150)))
st.pyplot(f)

f, ax = plt.subplots(figsize=(20, 8))
f.suptitle("Price vs Room types")
sns.histplot(data=df_unique_outliers,
            x='price',
            hue='room_type',
            ax=ax,
            multiple="stack",
            stat='count', bins=list(range(price_slider[0], price_slider[1], 50)))

ax.set_xticks(list(range(price_slider[0], price_slider[1], 50)))
st.pyplot(f)