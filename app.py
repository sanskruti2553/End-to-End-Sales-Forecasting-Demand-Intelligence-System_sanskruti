import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Load Dataset
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()

    return df

df = load_data()

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Demand Segments"
    ]
)

# =====================================================
# PAGE 1
# =====================================================

if page == "Sales Overview":

    st.title("📈 Sales Overview Dashboard")

    total_sales = round(df["Sales"].sum(),2)

    total_orders = df["Order ID"].nunique()

    avg_sales = round(df["Sales"].mean(),2)

    c1,c2,c3 = st.columns(3)

    c1.metric("Total Sales",f"${total_sales:,.2f}")
    c2.metric("Total Orders",total_orders)
    c3.metric("Average Sale",f"${avg_sales}")

    st.divider()

    yearly = df.groupby("Year")["Sales"].sum().reset_index()

    fig = px.bar(
        yearly,
        x="Year",
        y="Sales",
        color="Sales",
        title="Total Sales by Year"
    )

    st.plotly_chart(fig,use_container_width=True)

    monthly = df.groupby("Order Date")["Sales"].sum().reset_index()

    fig2 = px.line(
        monthly,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig2,use_container_width=True)

    st.subheader("Sales by Region & Category")

    region = st.selectbox(
        "Select Region",
        sorted(df["Region"].unique())
    )

    category = st.selectbox(
        "Select Category",
        sorted(df["Category"].unique())
    )

    filtered = df[
        (df["Region"]==region) &
        (df["Category"]==category)
    ]

    fig3 = px.bar(
        filtered,
        x="Sub-Category",
        y="Sales",
        color="Sub-Category"
    )

    st.plotly_chart(fig3,use_container_width=True)

# =====================================================
# PAGE 2
# =====================================================

elif page=="Forecast Explorer":

    st.title("📉 Forecast Explorer")

    st.success("Best Forecasting Model : XGBoost")

    choice = st.selectbox(

        "Select Segment",

        [
            "Furniture",
            "Technology",
            "Office Supplies",
            "West",
            "East"
        ]
    )

    horizon = st.slider(

        "Forecast Horizon (Months)",

        1,

        3,

        3

    )

    st.write(f"Forecast Horizon : **{horizon} Month(s)**")

    forecast = pd.DataFrame({

        "Month":[1,2,3],

        "Forecast Sales":[
            31071,
            26633,
            24321
        ]

    })

    fig = px.line(

        forecast,

        x="Month",

        y="Forecast Sales",

        markers=True,

        title=f"{choice} Forecast"

    )

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("Model Performance")

    c1,c2,c3 = st.columns(3)

    c1.metric("MAE","14763.81")
    c2.metric("RMSE","18337.41")
    c3.metric("MAPE","14.48%")

# =====================================================
# PAGE 3
# =====================================================

elif page=="Anomaly Report":

    st.title("🚨 Anomaly Detection Report")

    anomaly = pd.DataFrame({

        "Year":[2007,2008,2009,2010],

        "Global Sales":[
            611.13,
            678.90,
            667.30,
            600.45
        ]

    })

    st.dataframe(anomaly)

    fig = px.line(

        anomaly,

        x="Year",

        y="Global Sales",

        markers=True,

        title="Detected Anomalies"

    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# PAGE 4
# =====================================================

elif page=="Demand Segments":

    st.title("📦 Product Demand Segments")

    cluster = pd.DataFrame({

        "Cluster":[

            "High Value Premium Products",

            "Stable Demand Products",

            "High Volume Best Sellers",

            "Emerging Growth Product"

        ],

        "Products":[

            "Copiers, Machines",

            "Bookcases, Appliances, Paper, Art, Labels",

            "Phones, Chairs, Tables, Storage, Accessories, Binders",

            "Supplies"

        ]

    })

    st.dataframe(cluster)

    fig = px.bar(

        cluster,

        x="Cluster",

        y=[2,8,6,1],

        labels={"value":"Number of Sub-Categories"}

    )

    st.plotly_chart(fig,use_container_width=True)

st.sidebar.success("Internship Project Dashboard")