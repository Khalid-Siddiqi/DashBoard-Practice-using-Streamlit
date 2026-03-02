import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv(
    io = "supermarkt_sales.xlsx",
    engine= "openpyxl")