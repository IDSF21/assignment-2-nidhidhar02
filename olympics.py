import streamlit as st 
import pandas as pd 
import pydeck as pdk 
import matplotlib.pyplot as plt
from plotly import tools
import seaborn as sns
import altair as alt
from vega_datasets import data


def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

st.title('A quick glance at Tokyo Olympics 2020')
st.write('')
st.write('This dashboard analyses the performance of all countries participating in the Tokyo 2020 olympics. The <a href=https://www.kaggle.com/piterfm/tokyo-2020-olympics/version/2> dataset </a> for this task was got from Kaggle', unsafe_allow_html=True)
st.write('')
st.header('Let\'s first take a look at the overall distribution of medals across all countries')
country_codes = pd.read_csv('country_codes.csv',sep=',', encoding='latin-1')
country_codes.set_index('Alpha-3 code', inplace = True)

total_medal_count = load_data('total_medal_count_with_lat_and_long.csv')
total_medal_count.set_index('Country Code', inplace = True)
total_medal_count['id'] = country_codes['Numeric']

def draw_map(input_option='Total'):
    
    colors = {'Total':"lightgreyred",
                   'Gold Medal':"lightorange",
                   'Silver Medal':"lightgreyteal",
                   'Bronze Medal':"lightgreyred"}
    
    total_medal_count['Medals'] = total_medal_count[input_option]

    source = alt.topo_feature(data.world_110m.url, "countries")

    world_map = (
        alt.Chart(source, title=f'Countries by number of {input_option} medals')
        .mark_geoshape(stroke="black", strokeWidth=0.15)
        .encode(
            color=alt.Color(
                "Medals:N", 
                scale=alt.Scale(scheme=colors[input_option]), 
                legend=None),
            tooltip=[
                alt.Tooltip("Country:N", title="Team"),
                alt.Tooltip("Medals:Q", title="Medals"),
            ],
        )
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(total_medal_count, "id", ["Country", "Medals"]),
        )
    ).configure_view(strokeWidth=0).properties(width=700, height=400).project("naturalEarth1")
    
    return world_map

medal = st.selectbox('Select the type of medal whose distribution you wish to view',
               options = ['Gold Medal','Silver Medal','Bronze Medal','Total'])

st.write(draw_map(medal))

st.write('')
st.header('Now let\'s dive deeper into the performance of your country')

athletes = load_data('final_olympics_dataset_with_latitude_and_longitude.csv')
medals = load_data('total_medal_count_with_lat_and_long.csv')

country_name_input = st.selectbox(
    'Select the country whose statistics you wish to view',
    athletes['country'].unique())

if len(country_name_input) > 0:
    subset_athlete_data = athletes[athletes['country']==country_name_input]
    subset_medals_data = medals[medals['name']==country_name_input]


selected_rows = subset_athlete_data[~subset_athlete_data['medal_code']. isna()]

col1, col2 = st.columns(2)
with col1:
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{v:d}'.format(v=val)
        return my_format

    donut_labels = ['Gold Medals', 'Silver Medals', 'Bronze Medals']
    size = [subset_medals_data.iloc[0]['Gold Medal'], subset_medals_data.iloc[0]['Silver Medal'], subset_medals_data.iloc[0]['Bronze Medal']]
    my_circle = plt.Circle( (0,0), 0.7, color='white')

    fig1, ax1 = plt.subplots()
    plt.pie(size, labels=donut_labels, colors=['gold','silver','peru'], autopct=autopct_format(size))
    plt.gcf()
    plt.gca().add_artist(my_circle)
    fig1.suptitle("Distribution of medals by type")
    st.pyplot(fig1)


with col2:
    gender_data = selected_rows.groupby('gender').size().reset_index()
    # fig1, ax = plt.subplots(figsize=(15, 15))
    fig1, ax = plt.subplots()
    sns.barplot(x="gender", y=0, data=gender_data, color="maroon")
    ax.set(ylabel="Number of medals", xlabel="Gender")
    fig1.suptitle("Distribution of medals by gender")
    st.pyplot(fig1)


st.write('Let us also take a look at the top scoring athletes of', country_name_input)

k = st.slider("Enter top number of athletes you wish to see", 3, selected_rows.shape[0])

top_athletes = selected_rows.groupby('athlete_name').size().nlargest(k).reset_index()
f, ax = plt.subplots()
sns.barplot(x=0, y="athlete_name", data=top_athletes, color="maroon")
ax.set(ylabel="Athlete Name", xlabel="Number of medals")
f.suptitle("Top athletes by medals")
st.pyplot(f)


st.write('')
st.write('Finally, let us take a look at the top scoring disciplines for ', country_name_input)

k = st.slider("Enter top number of disciplines you wish to see", 3, selected_rows.shape[0])

top_disciplines = selected_rows.groupby('discipline').size().nlargest(k).reset_index()
f, ax = plt.subplots()
sns.barplot(x=0, y="discipline", data=top_disciplines, color="maroon")
ax.set(ylabel="Discipline", xlabel="Number of medals")
f.suptitle("Top disciplines by medals")
st.pyplot(f)
