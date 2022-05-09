import streamlit as st
import pandas as pd
f




st.title("UFO Data")
st.write("This shows the dataframe of the UFO Data set")
ufo_data = pd.read_csv(r"scrubbed.csv", low_memory=False)

st.write(ufo_data)

st.write("---")
st.header("Data Analysis")
ufo_data.datetime = ufo_data.datetime.map(lambda x: "00:00" if "24:00" in x else x)
ufo_data['datetime'] = pd.to_datetime(ufo_data['datetime'], errors='coerce')
ufo_data.insert(1, 'year', ufo_data['datetime'].dt.year)
ufo_data['year'] = ufo_data['year'].fillna(0).astype(int)
ufo_data['city'] = ufo_data['city'].str.title()
ufo_data['state'] = ufo_data['state'].str.upper()
ufo_data['latitude'] = pd.to_numeric(ufo_data['latitude'], errors='coerce')

shape = ufo_data.groupby(['shape', 'year'])['shape'].count().reset_index(name='count').sort_values(['count'], ascending=False)
print(shape)





