import streamlit

streamlit.title("Weather Forecast Application")

place = streamlit.text_input(label="Place", placeholder="Enter location")

number_of_days = streamlit.slider(label="Number of Days", min_value=1, max_value=5,
                                  help="Select the number of days to forecast.")

option_forecast = streamlit.selectbox("Select the data  you would like to view: ",
                                      options=("Temperature", "Sky"))

if place:
    streamlit.subheader(f"{option_forecast} for the next {number_of_days} days in {place}.")

