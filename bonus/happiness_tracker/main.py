import plotly
import streamlit
import pandas
import plotly.express as express


def get_data(y_data, x_data):
    y_data = dataframe[y_data].to_list()
    x_data = dataframe[x_data].to_list()
    return y_data, x_data


def draw_graph():
    data_y_axis, data_x_axis = get_data(column_y_axis, column_x_axis)
    line_graph = express.scatter(y=data_y_axis, x=data_x_axis,
                                 labels={"x": f"{column_x_axis}",
                                         "y": f"{column_y_axis}"})
    streamlit.plotly_chart(line_graph)


streamlit.title("In Search for Happiness")

dataframe = pandas.read_csv("D:/Udemy/PythonCourse/PythonExercise7/files/happy.csv")

data_columns = dataframe.columns[1:]

column_y_axis = streamlit.selectbox(label="Select the data for the y-axis: ",
                                    options=data_columns)

column_x_axis = streamlit.selectbox(label="Select the data for the x-axis: ",
                                    options=data_columns)

streamlit.subheader(f"{column_x_axis.title()} and {column_y_axis.title()}")
draw_graph()


