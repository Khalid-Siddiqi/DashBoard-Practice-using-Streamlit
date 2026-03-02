import pandas as pd
import plotly.express as px
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


#st.dataframe(df_selection)

## Main Page
st.title(":bar_chart: Supermarket Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")

# 2nd kpi : bar chart
sales_by_product_line = (
    df_selection.groupby(by=["Product line"])["Total"].sum().sort_values()
)
fig_product_sales = px.bar(
    sales_by_product_line,
    y=sales_by_product_line.index,
    x="Total",
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_product_sales, use_container_width=True)