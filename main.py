import streamlit
import plotly.express as express
import backend


def get_data(day_count):
    date_list_local = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temp_list_local = [10, 11, 15]
    temp_list_local = [day_count * i for i in temp_list_local]
    return date_list_local, temp_list_local


if __name__ == "__main__":
    streamlit.title("Weather Forecast Application")

    place = streamlit.text_input(label="Place", placeholder="Enter location")

    number_of_days = streamlit.slider(label="Number of Days", min_value=1, max_value=5,
                                      help="Select the number of days to forecast.")

    option_forecast = streamlit.selectbox("Select the data  you would like to view: ",
                                          options=("Temperature", "Sky"))

    if place:
        streamlit.subheader(f"{option_forecast} for the next {number_of_days} days in {place}.")
        data = backend.get_data(place, number_of_days, option_forecast)
        if data is None:
            pass
        elif option_forecast == "Temperature":
            plotly_figure = express.line(x=data.keys(), y=data.values(), labels={"x": "Date", "y": "Temperature"})
            streamlit.plotly_chart(plotly_figure)
        elif option_forecast == "Sky":
            image_paths = [f"files/images/{image}.png" for image in data.values()]
            streamlit.image(image_paths, width=150, caption=list(data.keys()))
