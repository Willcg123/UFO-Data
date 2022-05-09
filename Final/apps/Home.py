import streamlit as st
from PIL import Image
# ---- HEADER SECTION ----
def app():
    st.title("UFO Daya Analysis")
    st.subheader("This website will analyze a UFO Sightings Data set")
    st.write("The dataset can be found [here](https://www.kaggle.com/datasets/NUFORC/ufo-sightings)")
# ---- WHAT I WILL DO ----
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I will be looking for")
        st.write("##")
        st.write(
            """
            I will be looking at key variables found from the UFO dataset. These will include:
            - Sorting/filtering and data exploration of the UFO dataset
            - Heat map of UFO sigthings in the USA.
            - Years with the most UFO Sightings
            - Months and days with most UFO sightings
            - Specific shapes of the UFO sightings, sorted by year and country 
            """
        )

    with right_column:
        image = Image.open('UFO.jpg')
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(image, caption="Not a real picture")
