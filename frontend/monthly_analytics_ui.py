import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def monthly_analytics_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1), key="m_start")

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 9, 30), key="m_end")

    if st.button("Get Monthly Analytics"):

        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/monthly", json=payload)
        data = response.json()

        df = pd.DataFrame(data)

        st.title("Monthly Expense Trend")

        df["month"] = pd.to_datetime(df["month"])
        df["month"] = df["month"].dt.strftime("%B")
        st.bar_chart(df.set_index("month")["total"])

        st.table(df)