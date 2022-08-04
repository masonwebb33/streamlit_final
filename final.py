import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from statistics import mode
import datetime as dt


states = {'AL' : 'Alabama',
'AK' : 'Alaska',
'AZ' : 'Arizona',
'AR' : 'Arkansas',
'CA' : 'California',
'CO' : 'Colorado',
'CT' : 'Connecticut',
'DE' : 'Delaware',
'FL' : 'Florida',
'GA' : 'Georgia',
'HI' : 'Hawaii',
'ID' : 'Idaho',
'IL' : 'Illinois',
'IN' : 'Indiana',
'IA' : 'Iowa',
'KS' : 'Kansas',
'KY' : 'Kentucky',
'LA' : 'Louisiana',
'ME' : 'Maine',
'MD' : 'Maryland',
'MA' : 'Massachusetts',
'MI' : 'Michigan',
'MN' : 'Minnesota',
'MS' : 'Mississippi',
'MO' : 'Missouri',
'MT' : 'Montana',
'NE' : 'Nebraska',
'NV' : 'Nevada',
'NH' : 'New Hampshire',
'NJ' : 'New Jersey',
'NM' : 'New Mexico',
'NY' : 'New York',
'NC' : 'North Carolina',
'ND' : 'North Dakota',
'OH' : 'Ohio',
'OK' : 'Oklahoma',
'OR' : 'Oregon',
'PA' : 'Pennsylvania',
'RI' : 'Rhode Island',
'SC' : 'South Carolina',
'SD' : 'South Dakota',
'TN' : 'Tennessee',
'TX' : 'Texas',
'UT' : 'Utah',
'VT' : 'Vermont',
'VA' : 'Virginia',
'WA' : 'Washington',
'WV' : 'West Virginia',
'WI' : 'Wisconsin',
'WY' : 'Wyoming'
}

#read in data
df = pd.read_excel('ufo_sightings.xlsx')
df_filtered = df[['datetime','city','state', 'country','shape','duration (seconds)','comments']]
df_filteredCountry = df[['datetime','city','country','shape','duration (seconds)', 'comments']]
# streamlit setups
st.title('UFO sightings')


drop_options = []
# gives us sightings
df_country = df_filtered.groupby('country').count()
st.header('Quick UFO data facts!')

# years in dataset
numSightings = len(df)
st.write(f'There are {numSightings} sightings total in the dataset.')
# group by country--find largest country --
ausDF = df_filtered[(df_filteredCountry["country"] == 'au')]
aus_sightings = len(ausDF)
canDF = df_filtered[(df_filteredCountry["country"] == 'ca')]
can_sightings = len(canDF)
gbDF = df_filtered[(df_filteredCountry["country"] == 'gb')]
gb_sightings = len(gbDF)
germDF = df_filtered[(df_filteredCountry["country"] == 'de')]
germ_sightings = len(germDF)
usDF = df_filtered[(df_filteredCountry["country"] == 'us')]
us_sightings = len(usDF)


sightings = {
    'US':us_sightings,
    'Germany':germ_sightings,
    'UK':gb_sightings,
    'Canada':can_sightings,
    'Australia':aus_sightings
}
# list comps -- get key of highest value and lowest value
max_keys = [key for key, value in sightings.items() if value == max(sightings.values())]
min_keys = [key for key, value in sightings.items() if value == min(sightings.values())]
for i in max_keys:
    st.write(f'The country with the most amount of sightings is {i} with {sightings[i]} sightings.')
for i in min_keys:
    st.write(f'The country with the least amount of sightings is {i} with {sightings[i]} sightings.')
shapes = list(df_filtered['shape'])
st.write(f'The most common shape used to describe the UFOs is a {mode(shapes)}.')
# chart set up
bar_labels = []
bar_values = []
for country in sightings.keys():
    bar_labels.append(country)
for val in sightings.values():
    bar_values.append(val)

color_opt = st.sidebar.radio(label='select a color for the bars on the graph',options=['black','red','blue','green','yellow','cyan'])
width_opt = st.sidebar.slider(label='set the width of the bars', min_value= 0.5,max_value=1.0, step=.05)
fig1, ax1 = plt.subplots()
ax1.bar(bar_labels, bar_values,color = color_opt, width=width_opt)
ax1.set_title('Sightings in Each Country')
st.pyplot(fig1)
st.caption('As you can see from the graph, the US has the most sightings by a longshot.')

# country list
countrylst = ['Australia','Canada','Germany','United Kingdom','United States']
country = st.sidebar.selectbox(label = 'select a country for UFO sighting info',options = countrylst)
country_abv = ''
if country == 'Australia':
    country_abv = 'au'
    st.header(f'Data for sightings in {country}')
    country_df = (df_filteredCountry[(df_filteredCountry["country"] == country_abv)])
    dur = float(country_df['duration (seconds)'].mean())
    st.write(country_df)
    st.write(f'Average Duration: {dur:.2f}')
    st.write(f'Total sightings: {len(country_df)}')
    shapes = list(country_df['shape'])
    st.write(f'The most common shape used to describe the UFOs in {country} is a {mode(shapes)}.')
    country_map_df = (df[(df["country"] == country_abv)])
    country_coords = country_map_df[['latitude','longitude']]
    st.map(country_coords)
    #st.write(st.write(f"Average Duration for sightings: {country_df['duration (seconds)'].mean():.2f} seconds"))
elif country == 'Canada':
    country_abv = 'ca'
    st.header(f'Data for sightings in {country}')
    country_df = (df_filteredCountry[(df_filteredCountry["country"] == country_abv)])
    dur = float(country_df['duration (seconds)'].mean())
    st.write(country_df)
    st.write(f'Average Duration: {dur:.2f}')
    st.write(f'Total sightings: {len(country_df)}')
    shapes = list(country_df['shape'])
    st.write(f'The most common shape used to describe the UFOs in {country }is a {mode(shapes)}.')
    country_map_df = (df[(df["country"] == country_abv)])
    country_coords = country_map_df[['latitude','longitude']]
    st.map(country_coords)

elif country == 'Germany':
    country_abv = 'de'
    st.header(f'Data for sightings in {country}')
    country_df = (df_filteredCountry[(df_filteredCountry["country"] == country_abv)])
    dur = float(country_df['duration (seconds)'].mean())
    st.write(country_df)
    st.write(f'Average Duration: {dur:.2f}')
    st.write(f'Total sightings: {len(country_df)}')
    shapes = list(country_df['shape'])
    st.write(f'The most common shape used to describe the UFOs in {country} is a {mode(shapes)}.')
    country_map_df = (df[(df["country"] == country_abv)])
    country_coords = country_map_df[['latitude','longitude']]
    st.map(country_coords)

elif country == 'United Kingdom':
    country_abv = 'gb'
    st.header(f'Data for sightings in {country}')
    country_df = (df_filteredCountry[(df_filteredCountry["country"] == country_abv)])
    dur = float(country_df['duration (seconds)'].mean())
    st.write(country_df)


    st.write(f'Average Duration: {dur:.2f}')
    st.write(f'Total sightings: {len(country_df)}')
    shapes = list(country_df['shape'])
    st.write(f'The most common shape used to describe the UFOs in {country} is a {mode(shapes)}.')
    country_map_df = (df[(df["country"] == country_abv)])
    country_coords = country_map_df[['latitude','longitude']]
    st.map(country_coords)

#elif country == 'United States':
    #country_abv = 'us'

elif country == 'United States':
    country_abv = 'us'
    state_filter_opt = st.sidebar.radio(label = 'Filter by state?', options=['yes','no'])
    if state_filter_opt == 'no':
        st.header(f'Data for sightings in {country}')
        # dataframe grouped by country where the country is matching what the user selected
        country_df = (df_filtered[(df_filteredCountry["country"] == country_abv)])
        # average time in seconds for that country
        dur = float(country_df['duration (seconds)'].mean())
        st.write(country_df)
        st.write(f'Average Duration: {dur:.2f}')
        # number of sightings in the dataframe
        st.write(f'Total sightings: {len(country_df)}')
        shapes = list(country_df['shape'])
        # used mode to find the most common shape
        st.write(f'The most common shape used to describe the UFOs in {country} is a {mode(shapes)}.')
        # different df without lat and lon filtered out--matches country user selected
        country_map_df = (df[(df["country"] == country_abv)])
        country_coords = country_map_df[['latitude','longitude']]
        st.map(country_coords)

    elif state_filter_opt == 'yes':
        state = st.sidebar.selectbox(label='Select a State',options=states.keys())
        st.header(f'Data for sightings in {state}')
        # new df, getting only values for that state
        state_df = (df_filtered[(df_filtered["state"] == state.lower())])
        dur = float(state_df['duration (seconds)'].mean())
        st.write(state_df)
        st.write(f'Average Duration: {dur:.2f}')
        st.write(f'Total sightings: {len(state_df)}')
        shapes = list(state_df['shape'])
        st.write(f'The most common shape used to describe the UFOs in {state} is a {mode(shapes)}.')
        state_map_df = (df[(df["state"] == state.lower())])
        state_coords = state_map_df[['latitude','longitude']]
        st.map(state_coords)


