import streamlit as st
import pandas as pd
from collections import Counter
from gensim.parsing.preprocessing import remove_stopwords


def app():
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

    st.write("## Most Common Words in Comments")

    words = [i for i in ufo_data.comments.dropna()]
    words = " ".join(words)
    filtered = remove_stopwords(words)
    split = filtered.split()
    count_words = Counter(split)
    common = count_words.most_common(20)
    common_df = pd.DataFrame(common, columns=['Words', 'Amount'])

    st.write(common_df)

    st.write("## Sorted by duration")
    ufo_data['duration'] = ufo_data['duration'].str.extract('(\d+)', expand=False)
    ufo_data['duration'] = ufo_data['duration'].astype(float)

    sort_dur = ufo_data.sort_values(['duration'], ascending=False)
    st.write(sort_dur)

    st.write('## Filter for Waltham')
    waltham = ufo_data[ufo_data['city'] == 'Waltham']
    st.dataframe(waltham)

    st.write('## Group By Shape')
    shape = ufo_data.groupby(['shape'])['shape'].count().reset_index(name='count').sort_values(['count'], ascending=False)
    st.write(shape)

