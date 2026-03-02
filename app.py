import pandas as pd
#import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Supermarket Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_excel(
    'supermarkt_sales.xlsx',
    engine= "openpyxl",
    sheet_name= "Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000,
    )



# Building Sidebars now
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

costumer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options = df["Gender"].unique(),
    default = df["Gender"].unique()
)
df_selection = df.query(
    "City == @city & Customer_type == @costumer_type & Gender == @gender"
)


st.dataframe(df_selection)