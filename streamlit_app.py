import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Customer Analytics Dashboard")
df = pd.read_csv("dashboard_customer/customers (1).csv")
st.sidebar.header("Filter Data")
departments = st.sidebar.multiselect(
    "Pilih Departments",
    df["Department"].dropna().unique()
)
genders = st.sidebar.multiselect(
    "Pilih Gender",
    df["Gender"].dropna().unique()
)
st.sidebar.header("Filter Rentang Umur")
min_usia, max_usia = int(df["Age"].min()), int(df["Age"].max())
usia_range = st.sidebar.slider(
    "Usia",
    min_value=min_usia,
    max_value=max_usia,
    value=(min_usia, max_usia)
)
df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["Gender"].isin(genders)) &
    (df["Age"].between(usia_range[0], usia_range[1]))
]
st.subheader("Data Tabel")
st.dataframe(df_filtered)
st.subheader("Visualisasi Statistik")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribusi Gender")
    pie_gender = px.pie(
        df_filtered,
        names="Gender",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    pie_gender.update_layout(
    width=350,
    height=350
)
    st.plotly_chart(pie_gender)
    with col2:
        st.subheader("Gaji Rata-rata per Department")

    salary_dept = (
        df_filtered
        .groupby("Department")["AnnualSalary"]
        .mean()
        .reset_index()
    )

    bar_salary = px.bar(
        salary_dept,
        x="Department",
        y="AnnualSalary",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(bar_salary)

st.subheader("Rata-rata Gaji Berdasarkan Usia")
salary_age = (
    df_filtered
    .groupby("Age")["AnnualSalary"]
    .mean()
    .reset_index()
    .sort_values("Age")
)

line_age = px.line(
    salary_age,
    x="Age",
    y="AnnualSalary",
    markers=True
)

st.plotly_chart(line_age)

st.subheader("Proporsi Jumlah Customer per Department")

dept_count = (
    df_filtered["Department"]
    .value_counts()
    .reset_index()
)

dept_count.columns = ["Department", "Jumlah Customer"]

donut_dept = px.pie(
    dept_count,
    names="Department",
    values="Jumlah Customer",
    hole=0.45,
    color="Department",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

donut_dept.update_layout(
    height=350,
    width=350,
    margin=dict(t=40, b=40, l=40, r=40),
    legend=dict(
        orientation="h",
        y=-0.2,
        x=0.5,
        xanchor="center"
    )
)

st.plotly_chart(donut_dept, use_container_width=False)
