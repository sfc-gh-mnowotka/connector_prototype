import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

home_tab, ingestion_tab, settings_tab = st.tabs(["Home", "Data Ingestion", "Settings"])

with home_tab:
    st.subheader("Ingestion timeline", help="This is a subheader")
    dates = pd.date_range('20230101', periods=100)
    df = pd.DataFrame(np.random.randn(100, 1), index=dates, columns=['Data transfer rate [GB]'])

    st.line_chart(df)

    column_left, column_right = st.columns([3, 1])

    with column_left:
        st.subheader("Daily credit consumption", help="This is a subheader")
        df = pd.DataFrame({
            'dates': pd.date_range('20230101', periods=100),
            'values': np.random.randn(100),
        })

        fig = px.bar(df, x='dates', y='values', color='values', color_continuous_scale='Reds')
        st.plotly_chart(fig, use_container_width=True)

    with column_right:
        st.subheader("Data Anomalies", help="This is a subheader")
        categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
        df = pd.DataFrame({
            'Category': np.random.choice(categories, 500),  # randomly picks a category for each row
        })

        df_count = df['Category'].value_counts().reset_index()
        df_count.columns = ['Category', 'Count']

        fig = px.pie(df_count, values='Count', names='Category', color_discrete_sequence=px.colors.sequential.Plasma)

        st.plotly_chart(fig, use_container_width=True)

with ingestion_tab:
    col_1, col_2, col_3, col_4, _ = st.columns([1, 1, 1, 1, 6])

    with col_1:
        st.button("🔎", key="search")
    with col_2:
        st.selectbox("Type", ["Ongoing", "Completed", "Failed", "Queued"], key="type")
    with col_3:
        st.selectbox("Status", ["All", "Success", "Failure"], key="status")
    with col_4:
        st.markdown("1 342 properties")

    df = pd.DataFrame(
        [
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
            {"select": False, "property_name": "favorable-iris-344415 / 307369781", "sync_every": "1 hour",
             "more": "..."},
        ]
    )
    edited_df = st.data_editor(
        df,
        column_config={
            "select": "",
            "property_name": st.column_config.TextColumn(
                "PROPERTY NAME",
                width="large",
                disabled=True,
            ),
            "sync_every": st.column_config.SelectboxColumn(
                "SYNC EVERY",
                width="large",
                options=[
                    "1 week",
                    "1 day",
                    "1 hour",
                    "1 day",
                    "15 min",
                    "1 min"
                ],
                required=False,
                default=None
            ),
            "more": ""
        },
        hide_index=True,
    )

    with settings_tab:
        col_settings_1, col_settings_2, _ = st.columns([2, 6, 2])

        with col_settings_1:
            st.subheader("Settings")

            st.markdown("""
            1. [Configure](#)
            2. [Authentication](#)
            3. [Email alerts](#)
            4. [Manage access](#)
            """)

        with col_settings_2:
            st.subheader("Connector Objects", help="This is a subheader")
            st.text("Objects created to install, manage and view the connector.")

            st.divider()

            col_objects_1, col_objects_2 = st.columns(2)

            with col_objects_1:
                st.markdown("**Database**")
            with col_objects_2:
                st.markdown("💾 BQ_ANALYTICS_WAREHOUSE")

            st.divider()

            st.text("Objects created to run the ingestions.")

            col_wh_1, col_wh_2 = st.columns(2)

            with col_wh_1:
                st.markdown("**Warehouse**")
            with col_wh_2:
                st.markdown("🏭 BQ_BIGQUERY_WH")

            col_db_1, col_db_2 = st.columns(2)

            with col_db_1:
                st.markdown("**Destination Database**")
            with col_db_2:
                st.markdown("💾 BQ_BIGQUERY")

            col_schema_1, col_schema_2 = st.columns(2)

            with col_schema_1:
                st.markdown("**Schema**")
            with col_schema_2:
                st.markdown("📑 BQ_ABIGQUERY.PUBLIC")

            col_role_1, col_role_2 = st.columns(2)

            with col_role_1:
                st.markdown("**Role**")
            with col_role_2:
                st.markdown("👤  BQ_BIGQUERY_ADMIN")
