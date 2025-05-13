import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("COVID-19 Tracker Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv", parse_dates=["date"])
    df = df[df["location"].isin(["Kenya", "India", "United States"])]
    return df

df = load_data()

country = st.selectbox("Select a Country", df["location"].unique())

date_range = st.slider("Select Date Range",
                       min_value=df["date"].min().date(),
                       max_value=df["date"].max().date(),
                       value=(df["date"].min().date(), df["date"].max().date()))

filtered = df[(df["location"] == country) &
              (df["date"].dt.date.between(*date_range))]

st.line_chart(filtered.set_index("date")[["total_cases", "total_deaths", "total_vaccinations"]])
