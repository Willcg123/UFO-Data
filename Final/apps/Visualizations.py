import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


def app():
    st.title("UFO Data Analysis and Visualizations")
    ufo_data = pd.read_csv(r"scrubbed.csv", low_memory=False)

    ufo_data.datetime = ufo_data.datetime.map(lambda x: "00:00" if "24:00" in x else x)
    ufo_data['datetime'] = pd.to_datetime(ufo_data['datetime'], errors='coerce')
    ufo_data.insert(1, 'year', ufo_data['datetime'].dt.year)
    ufo_data['year'] = ufo_data['year'].fillna(0).astype(int)
    ufo_data['city'] = ufo_data['city'].str.title()
    ufo_data['state'] = ufo_data['state'].str.upper()
    ufo_data['latitude'] = pd.to_numeric(ufo_data['latitude'], errors='coerce')

    ufo_peryear = ufo_data.datetime.dt.year.value_counts()
    ufo_years = ufo_peryear.index
    ufo_values_peryear = ufo_peryear.values

    year_fig = plt.figure(figsize=(10, 8))
    plt.bar(ufo_years, ufo_values_peryear)
    plt.xlabel("year")
    plt.ylabel("Number of UFO Sightings")
    plt.title("Number of UFO Sightings Per Year World Wide")
    plt.xticks(ufo_years, rotation=70)
    plt.xticks(fontsize=6)
    plt.xlim(1965, 2013)

    st.pyplot(year_fig)

    month_fig = plt.figure(figsize=(15, 8))

    ax = sns.countplot(ufo_data.datetime.dt.month)
    plt.title("UFO Sigthings by Month")
    ax.set(xlabel='Month', ylabel='Number of UFO sightings')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()+50))

    st.pyplot(month_fig)

    day_fig = plt.figure(figsize=(15, 8))

    day_x = sns.countplot(ufo_data.datetime.dt.day)
    plt.title("UFO Sigthings by Month")
    day_x.set(xlabel='Month', ylabel='Number of UFO sightings')
    for p in day_x.patches:
        day_x.annotate(str(p.get_height()), (p.get_x(), p.get_height() + 10))

    st.pyplot(day_fig)

    ufo_state = ufo_data[ufo_data.country == "us"]["state"].value_counts().index
    states_values = ufo_data[ufo_data.country == "us"]["state"].value_counts().values
    ufo_state = [i.upper() for i in ufo_state]
    ufo_scale = [[0, 'rgb(255, 217, 251)'], [1, 'rgb(255, 3, 228)']]

    data = [
        dict(
            type='choropleth',
            autocolorscale=False,
            colorscale=ufo_scale,
            locations=ufo_state,
            z=states_values,
            locationmode='USA-states',
            text="times",
            marker=dict(
                line=dict(
                    color='rgb(255,255,255)',
                    width=2
                )),
            colorbar=dict(
                title="Number of UFO Sightings")
        )
    ]

    layout = dict(
        title='UFO sigthings by State (1910-2014)',
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
    )

    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)





