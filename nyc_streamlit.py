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

import pydeck as pdk

# Outline:
# 0. Big question
# 1. Airbnb introduction
# 2. COVID - Why still airbnb?
#     Unique places with unique experience;
#     Time to relax a bit, but still follow COVID rules.
# 3. How to choose an airbnb:
#     Review Scores;
#     Price ranges: Neighborhood, Accommodate types;
#     Locations - Safety: Crime Rate, COVID Rate.
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

# NYC_Covid_Daily_CSV
nyc_covid_daily_oct_2020 = load_data('https://raw.githubusercontent.com/duongtruongtrong/CoderSchool_week_3_project_duong_huyto/master/nyc_covid_daily_oct_2020.csv')
nyc_covid_daily_oct_2020['Date'] = pd.to_datetime(nyc_covid_daily_oct_2020['DATE_OF_INTEREST'])

# NYC_Covid_Daily_Chart

plt.rc('font', size=18) #controls default text size
plt.rc('axes', titlesize=22) #fontsize of the title
plt.rc('axes', labelsize=22) #fontsize of the x and y labels
plt.rc('xtick', labelsize=22) #fontsize of the x tick labels
plt.rc('ytick', labelsize=22) #fontsize of the y tick labels
plt.rc('legend', fontsize=22) #fontsize of the legend

covid, ax = plt.subplots(figsize=(18, 8))

covid.suptitle('New York Daily New COVID-19 Cases', fontsize=25)

sns.lineplot(x='Date', y='Cases', data=nyc_covid_daily_oct_2020, ax=ax, label='Daily')
sns.lineplot(x='Date', y='7-day average', data=nyc_covid_daily_oct_2020, ax=ax, label='7-day average')
ax.grid(True)

st.pyplot(covid)

st.markdown('### Number of new COVID cases in New York is stable around 1000 cases/day, and decreasing.')
st.markdown('## It is about time to get away and relax **safely**!')

covid_image = Image.open('covid.jpg')
st.image(covid_image, use_column_width = True)

st.write('We are **restricted to travel** ever since the pandemic started. Therefore, the **best option** we have is to travel **around our area**.')

# Airbnb in COVID reasons
st.subheader('You are a New Yorker')
st.markdown('- **Rarely** go to the other side of your city;')
st.markdown('- Or **visit other cities** in New York.')

st.subheader('Live As a Local with Unique Experience')
st.markdown('- **Unique experience** with Airbnb that traditional hotels cannot provide.')
st.markdown('- **Immersing you in the local culture** than getting a traditional hotel room')

st.subheader('Meet People')
st.markdown('Airbnb gives you the option to **stay with the local host**. The host will often be happy to welcome you and to tell you every interesting thing about the place you visit.')

st.subheader('Save Money')
st.markdown('_(sometimes)_')

st.markdown('- Airbnbs are usually **cheaper** than traditional hotels _(depends on the location)_')
st.markdown('- **Travel in a group**, Airbnb is definitely cheaper than a traditional hotel.')

# 3. How to choose an airbnb:
st.header('3. How To choose the best unique Airbnb?')

# 3.1 Current number of airbnb listings in NYC: Chart and xlsx
df_meaningful_col_light = load_data('https://raw.githubusercontent.com/duongtruongtrong/CoderSchool_week_3_project_duong_huyto/master/cleansed_listings_meaningful_2020_light.xlsx')

total_number_aribnb, ax = plt.subplots(figsize=(2, 1))
total_number_aribnb.suptitle('Current number of Airbnb in New York\n(until 2020-09-09)', fontsize=15)
ax.text(x=0.1, y=0, s='{:,}'.format(len(df_meaningful_col_light)), fontsize=30)
ax.axis("off")

st.pyplot(total_number_aribnb)

st.markdown('# Let us help you choose in a data way!')
st.markdown('_No recommendation airbnb places based on your interior design interest._')

# 3.2 Unique Airbnb concept
st.subheader('What is unique Airbnb?')
st.markdown('Airbnb with reviews **containing the word "unique"** and its synonyms: distinctive, special, extraordinary.')

st.markdown('**Example**:')
df_sample_review = load_data('review_sample.xlsx')
st.dataframe(df_sample_review)

st.markdown('''**"Unique" Review of listing id 9576478**: Vitaliy provided very informative directions and instructions on getting into the apartment. The apartment was exactly like it was in the photos. Harlem is a **unique** neighbourhood in NYC and will give you a different flavour of the city.''')

st.markdown('''**"Unique" Review of listing id 27930717**: The location of this apartment is great - very close to the subway and it allows you to reach Manhattan quickly. Good restaurants in the neighborhood. Maxime's (Hidden by Airbnb) , who were at home when we stayed, were absolutely fantastic and they made our experience in NYC **special**.''')

# Poplular words in "unique" review
st.markdown('**Poplular words in "unique" review**')
popular_word_image = Image.open('popular_words_unique_review.png')
st.image(popular_word_image, use_column_width = True)

st.subheader('Why unique Airbnb?')
st.markdown('You are **a New Yorker**.')
st.markdown('- Already too familiar to New York.')
st.markdown('- You need something **new**, something **unique** around New York.')

# Airbnb total review distribution chart
st.subheader('Number of "unique" reviews.')

unique_review, ax = plt.subplots(figsize=(20, 5))
unique_review.suptitle('Number of "Unique" Reviews Distribution', fontsize=25)

sns.boxplot(data=df_meaningful_col_light[(df_meaningful_col_light['total_unique_reviews']!=0) & (df_meaningful_col_light['total_unique_reviews'].notnull())],
            x='total_unique_reviews',
            ax=ax)
ax.set_xticks(list(range(0, 8, 2)) + list(range(10, 136, 25)))

st.pyplot(unique_review)

st.markdown('Most of Aibnb has **1 or 2 "unique" reviews**, which is **too small**.')
st.markdown('The more "unique" reviews the Airbnb has, the more authentically unique the Airbnb is.')
st.markdown('The **number of "unique" reviews** should be **over the upper whisker point** to be called a unique Aribnb.')

st.markdown('Not using "unique" review rate because:')
st.markdown('- High "unique" review rate does not mean the place is really unique, there may be only a few reviews in total.')
st.markdown('- A unique listings only need to be unique to some people')
st.markdown('- In addition, if the place is unique, most of reviewers only describe the place rather than mentioning the word "unique".')

# Current number of airbnb listings in NYC: Chart and xlsx
df_unique_outliers = load_data('https://raw.githubusercontent.com/duongtruongtrong/CoderSchool_week_3_project_duong_huyto/master/nyc_unique_aibnb.xlsx')

total_number_unique_aribnb, ax = plt.subplots(figsize=(2, 1))

total_number_unique_aribnb.suptitle('Total number of unique Airbnb in New York', fontsize=15)

ax.text(x=0.1, y=0, s='{:,}'.format(len(df_unique_outliers)), fontsize=30)

ax.axis("off")

st.pyplot(total_number_unique_aribnb)

# 3.2 Review Score of Unique Airbnb
st.subheader('Review Scores of "Unique" Airbnb')

review_list = ['overall', 'cleanliness', 'location', 'communication', 'checkin', 'accuracy']

review_score_list = []

# review_scores_value
# review_scores_cleanliness
# review_scores_location
# review_scores_communication
# review_scores_checkin
# review_scores_accuracy

review_score_list.append(df_unique_outliers['review_scores_value'].mean())
review_score_list.append(df_unique_outliers['review_scores_cleanliness'].mean())
review_score_list.append(df_unique_outliers['review_scores_location'].mean())
review_score_list.append(df_unique_outliers['review_scores_communication'].mean())
review_score_list.append(df_unique_outliers['review_scores_checkin'].mean())
review_score_list.append(df_unique_outliers['review_scores_accuracy'].mean())

cleanliness, ax = plt.subplots(figsize=(20, 5))
cleanliness.suptitle("Average Review Scores", fontsize=25)
sns.barplot(x=review_list, y=review_score_list, ax=ax)

ax.set_ylabel('Scores')

"""Attach a text label above each bar in *rects*, displaying its height."""
for i, j in zip(range(0, len(review_list)), review_score_list):
    ax.annotate(round(j, 1),
                xy=(i, j),
                # xytext=(2,-5),  # 2 points horizontal and -5 points vertial offset
                # textcoords="offset points",
                ha='center')

st.pyplot(cleanliness)

st.markdown('## Quality is secured.')
st.markdown('Review score of "unique" Airbnb are high.')

# 3.3 Price Range with: Neighborhood and Room types
st.subheader('Price Ranges of "Unique" Airbnb')

price_range, ax = plt.subplots(figsize=(20, 5))
price_range.suptitle("Price Ranges", fontsize=25)
sns.boxplot(data=df_unique_outliers,
            x='price',
            ax=ax)
ax.set_xticks(list(range(0, 701, 100)) + list(range(700, 2701, 400)))
st.pyplot(price_range)

st.markdown('Most "unique" Airbnb have price under 200 USD.')
st.markdown('The upper whisker point is around 350 USD, rounding it down to 300 USD as the first breaking point of "unique" Airbnb price ranges:')
st.markdown('**0-300**: Reasonable Price (round down from the upper whisker point)')
st.markdown('**Over 300**: Comming to Luxury')

# 3.3.1 Price Distribution in Term of Neighborhood
st.subheader('Price Distribution')

max_price = df_unique_outliers['price'].max()
min_price = df_unique_outliers['price'].min()

price_slider = st.slider("Choose a Price Range (USD)", 0, round(int(max_price), -1), (0, 300), 10)
bins_price = list(range(price_slider[0], price_slider[1] + 1, 50))

# for clearer xticks, when over 1000 USD the intervals must be 200 (instead of 100)
if price_slider[1] > 1000 and price_slider[0] < 1000:
    xticks_price = list(range(price_slider[0], 901, 100)) + list(range(900, price_slider[1], 200))
elif price_slider[1] > 1000 and price_slider[0] > 1000:
    xticks_price = list(range(price_slider[0], price_slider[1] + 1, 200))
else:
    xticks_price = list(range(price_slider[0], price_slider[1] + 1, 100))

price_neighborhood_room_type, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 27), constrained_layout=True)
sns.histplot(data=df_unique_outliers,
            x='price',
            hue='neighbourhood_group_cleansed',
            ax=ax1,
            multiple="stack",
            stat='count', bins=bins_price
            )
ax1.set_title("Price vs Neighborhood", fontsize=25)
ax1.set_xticks(xticks_price)

sns.histplot(data=df_unique_outliers,
            x='price',
            hue='room_type',
            ax=ax2,
            multiple="stack",
            stat='count', bins=bins_price)
ax2.set_title("Price vs Room types", fontsize=25)
ax2.set_xticks(xticks_price)

sns.histplot(data=df_unique_outliers,
            x='price',
            hue='bathrooms_type',
            ax=ax3,
            multiple="stack",
            stat='count', bins=bins_price)
ax3.set_title("Price vs Bathoom types", fontsize=25)
ax3.set_xticks(xticks_price)

st.pyplot(price_neighborhood_room_type)

st.markdown('There are plenty of Airbnb in **Manhattan and Brooklyn** with **private room or entire home/appartment** with **affordable price**.')
st.markdown('**Private room and entire home/appartment** are prioritized to **minimize COVID** transmission from strangers.')

# 3.4 Location
st.subheader('Location: Where is safe?')
st.markdown('### COVID cases and Crime cases around 25$km^2$ area around an Airbnb.')

def ax_barh(ax, x, y, x_label, y_label, align='center', height=0.8, reverse_y=True, label=None, title=None, data_label_format='{}', grid=True, data_label=True):

    def human_format(num, round_to=2):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num = round(num / 1000.0, round_to)
        return '{:.{}f}{}'.format(round(num, round_to), round_to, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

    def autolabel(rects, data_label_format=data_label_format):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            width = rect.get_width()
            height = rect.get_height()

            for x_data, y_data in zip(x,y):
                if data_label_format != 'human_format':
                    label = data_label_format.format(width) # format data label
                else: 
                    label = human_format(width)

            ax.annotate(label,
                        xy=(width, rect.get_y() + height / 1.5),
                        # xytext=(2,-5),  # 2 points horizontal and -5 points vertial offset
                        # textcoords="offset points",
                        ha='left')
    rects = ax.barh(y, x, 
            align=align,
            # Alignment of the base to the y coordinates*:
            #   'center': Center the bars on the y positions.
            #   'edge': Align the bottom edges of the bars with the y positions.
            # To align the bars on the top edge pass a negative height and align='edge'.

            height=height,
            # float or array-like, default: 0.8
            # The heights of the bars.
            
            label=label
            )
    if reverse_y==True:
        ax.invert_yaxis()

    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.grid(grid)

    if data_label == True:
        autolabel(rects)

# https://medium.com/@ahmetemin.tek.66/build-a-data-science-web-app-with-streamlit-and-python-4a9bdba35449
midpoint = [np.average(df_unique_outliers['latitude']), np.average(df_unique_outliers['longitude'])]

df_unique_outliers['covid_case_rate'] = df_unique_outliers['covid_case_rate'].round(1)
df_unique_outliers['total_crime_per_day'] = df_unique_outliers['total_crime_per_day'].round(1)

df_covid_top20 = df_unique_outliers.groupby('id').agg(total_covid=('covid_case_rate', 'sum')).sort_values(by='total_covid', ascending=False).head(20).reset_index()

df_crime_top20 = df_unique_outliers.groupby('id').agg(total_crime=('total_crime_per_day', 'sum')).sort_values(by='total_crime', ascending=False).head(20).reset_index()

covid, ax = plt.subplots(figsize=(10, 10))
covid.suptitle('Top 20 Most COVID Airbnb', fontsize=25)

ax_barh(ax, df_covid_top20['total_covid'], df_covid_top20['id'].astype(str), 'COVID cases per 100k people', 'Airbnb listing id', data_label_format="{:,}")

st.pyplot(covid)

crime, ax = plt.subplots(figsize=(10, 10))
crime.suptitle('Top 20 Most Crime Airbnb', fontsize=25)

ax_barh(ax, df_crime_top20['total_crime'], df_crime_top20['id'].astype(str), 'Number of crime per day', 'Airbnb listing id', data_label_format="{:,}")

st.pyplot(crime)

avg_covid_crime, (ax1, ax2) = plt.subplots(2, 1, figsize=(2, 2), constrained_layout=True)


df_covid = load_data('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/data-by-modzcta.csv')
avg_covid_case_rate = df_covid['COVID_CASE_RATE'].mean()

ax1.set_title('Average New York COVID Cases per 100k People', fontsize=15)
ax1.text(x=0.1, y=0.4, s='{:.1f}'.format(avg_covid_case_rate), fontsize=30)
ax1.axis("off")

avg_total_crime_per_day = df_unique_outliers['total_crime_per_day'].mean()

ax2.set_title('Average New York Crime Cases per Day', fontsize=15)
ax2.text(x=0.35, y=0.4, s='{:.1f}'.format(avg_total_crime_per_day), fontsize=30)
ax2.axis("off")

st.pyplot(avg_covid_crime)

st.markdown('**Overall Distribution Map**')
st.markdown('Each bar represent COVID cases and Crime cases around 25$km^2$ area around an Airbnb.')

# COVID Map
st.markdown('**COVID Map of each Airbnb**')
st.pydeck_chart(pdk.Deck(
                        initial_view_state={
                            'latitude': midpoint[0],
                            'longitude': midpoint[1],
                            'zoom': 11,
                            'pitch': 50
                        },
                        layers=[
                            pdk.Layer(
                                'HexagonLayer',
                                data=df_unique_outliers[['covid_case_rate', 'latitude', 'longitude']],
                                get_position=['longitude', 'latitude'],
                                auto_highlight=True,
                                radius=40,
                                elevation_scale=4,
                                elevation_range=[0, 500],
                                pickable=True,
                                extruded=True,
                                coverage=0.6,
                                getElevationWeight='covid_case_rate'
                            ),
                        ],
                        tooltip={
                                'html': "<b>COVID Case per 100k people:</b> {elevationValue}",
                                'style': {
                                    'color': 'white'
                                }
                            }
))

# Crime map
st.markdown('**Crime Map of each Airbnb**')
st.pydeck_chart(pdk.Deck(
                        initial_view_state={
                            'latitude': midpoint[0],
                            'longitude': midpoint[1],
                            'zoom': 11,
                            'pitch': 50
                        },
                        layers=[
                            pdk.Layer(
                                'HexagonLayer',
                                data=df_unique_outliers[['total_crime_per_day', 'latitude', 'longitude']],
                                get_position=['longitude', 'latitude'],
                                auto_highlight=True,
                                radius=40,
                                elevation_scale=4,
                                elevation_range=[0, 500],
                                pickable=True,
                                extruded=True,
                                coverage=0.6,
                                getElevationWeight='total_crime_per_day'
                            ),
                        ],
                        tooltip={
                                'html': "<b>Number of crime per day:</b> {elevationValue}",
                                'style': {
                                    'color': 'white'
                                }
                            }
))

# 4. Short List
st.subheader('Result: Short List of Unique Airbnb')
st.markdown('**Requirements**:')
st.markdown('- Price: **under 300 USD**, the affordable price.')
st.markdown('- Room type: **entir home/apt or private room or hotel room** with **private bathroom**, minimize COVID transmission.')
st.markdown('- COVID cases per 100k: **under New York average COVID cases** per 100k people.')
st.markdown('- Crime cases: **under the average crime cases** per day.')
st.markdown('- Host location: **local host**, for local unque experience.')

st.markdown('## Safety first!')

df_unique_outliers['cleansed_room_type'] = 'Shared'
df_unique_outliers['cleansed_room_type'][(df_unique_outliers['room_type'].isin(['Entire home/apt', 'Hotel room', 'Private room']) & (df_unique_outliers['bathrooms_type']=='private'))] = 'Private'

df_unique_outliers['is_local_host'][df_unique_outliers['is_local_host']=='t'] = 'Local Host'
df_unique_outliers['is_local_host'][df_unique_outliers['is_local_host']=='f'] = 'Not Local Host'

columns_list = ['id',
'listing_url',
'host_location',
'neighbourhood_cleansed',
'neighbourhood_group_cleansed',
'room_type',
'accommodates',
'price',
'bathrooms_number',
'bathrooms_type',
'price_per_person',
'is_local_host',
'total_unique_reviews',
'covid_case_rate',
'total_crime_per_day',
'latitude',
'longitude'
]
room_type_selector = st.selectbox("Select Room Type - Default: Private", df_unique_outliers['cleansed_room_type'].unique(), index=1)
local_host_selector = st.selectbox("Select Host Type - Default: Local Host", df_unique_outliers['is_local_host'].unique(), index=0)

price_slider = st.slider("Price Range (USD) - Default: 0-300", 0, round(int(max_price), -1), (0, 300), 10)

max_covid = df_unique_outliers['covid_case_rate'].max()
max_crime = df_unique_outliers['total_crime_per_day'].max()

covid_rate = st.slider("COVID cases (per 100k people) - Default: {:.1f}".format(avg_covid_case_rate), 0.0, max_covid, float(avg_covid_case_rate))

crime_rate = st.slider("Crime cases (per day) - Default: {:.1f}".format(avg_total_crime_per_day), 0.0, max_crime, float(avg_total_crime_per_day))

df_short_list = df_unique_outliers[columns_list][(df_unique_outliers['price'] >= price_slider[0]) 
                                                  & (df_unique_outliers['price'] <= price_slider[1])
                                                  & (df_unique_outliers['cleansed_room_type'] == room_type_selector)
                                                  & (df_unique_outliers['is_local_host'] == local_host_selector)
                                                  & (df_unique_outliers['covid_case_rate'] <= covid_rate)
                                                  & (df_unique_outliers['total_crime_per_day'] <= crime_rate)
                                                  ]

df_short_list

# Location
st.map(df_short_list[['latitude', 'longitude']], use_container_width=True)

st.markdown('## Only 1 place can meet all of the requirements.')

# 5. Project difficulty
st.subheader('Project difficulty')
st.markdown('- Limited in showing more information in tooltips of Airbnb on map. Can only 1 aggerated number.')
st.markdown('- Detecting synonyms of the word "unique" in reviews: "special" appear in "especial" -> Had to re-run everything.')
st.markdown('- Matching COVID data and crime data to Airbnb data set via latitude and longitude, they are not 1-1 match.')