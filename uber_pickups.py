from logging import getLogger

import streamlit as st
import numpy as np
import pandas as pd

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

logger = getLogger(__name__)


@st.cache
def load_data(nrows: int) -> pd.DataFrame:
    """
    Load uber data and do simple transformations:
    - columns lowered
    - date fields converted to datetime
    """
    logger.info('feching data from source..')
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    return data


def filter_dataframe(slider_value: int) -> None:
    """
    Filter data by the hour.
    """
    st.subheader(f'Map of all pickups at {slider_value}:00')
    filtered_data = data[data[DATE_COLUMN].dt.hour == slider_value]
    st.map(filtered_data)


# Adding a title.
st.title('Uber Pickups in NYC')
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
# data loaded from cache
data_load_state.text("Done! (using st.cache)")
if st.checkbox('Show raw data'):
    # section
    st.subheader('Raw data')
    # write data to the app
    st.write(data)
# add graph
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# add bar chart
st.bar_chart(hist_values)
# add to a map
st.subheader('Map of all pickups')
# load data to the map
st.map(data)
# add to a filtered map


# add the control to change the map
# min: 0h, max: 23h, default: 17h
hour_to_filter = st.slider('hour', 0, 23, 17)
filter_dataframe(hour_to_filter)
