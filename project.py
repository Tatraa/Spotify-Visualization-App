import streamlit as st
import pandas as pd
import numpy as np



person = {'name': 'Alice', 'age': 25}


numbers = {1, 2, 3, 4, 5}


class Chart:
    def __init__(self,chart_type,data_frame):
        self.type_of_charts = ["area_chart","bar_chart","line_chart"]
        self.chart_type = chart_type


        if chart_type in self.type_of_charts:
            user_choice_x = st.radio("X-", [i for i in data_frame.keys()])
            user_choice_y = st.radio("Y-", [i for i in data_frame.keys()])
            if chart_type == "area_chart":

                st.area_chart(data_frame,x=user_choice_x,y=user_choice_y)

            if chart_type == "bar_chart":
                st.bar_chart(data_frame,x=user_choice_x,y=user_choice_y)

            if chart_type == "line_chart":
                st.line_chart(data_frame,x=user_choice_x,y=user_choice_y)
        else:
            st.warning("Option Not Available",)



def main():
    type_of_charts = {"Area Chart":"area_chart", "Bar Chart":"bar_chart", "Line Chart":"line_chart","Plotly Char":"plotly_chart"}

    df = pd.read_csv("csvs/StudentsPerformance.csv")
    st.title("Students Performance")
    user_choice_type_of_chart = st.radio("Choose Type Of Data", type_of_charts)
    chart = Chart(type_of_charts[user_choice_type_of_chart], df)
    user_choice_type_of_chart = st.radio("Choose Type Of Data", [i for i in df.keys()])


main()
#
# st.dataframe(df)
# st.table(df.iloc[0:10])
# st.metric('My Metric',42,2)
