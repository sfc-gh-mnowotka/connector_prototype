import streamlit as st

st.set_page_config(layout="centered")

st.header("Configure Connector")

st.markdown("""
To complete the configuratin and run connector, the following objects will be created in your Snowflake environment [Learn More](#)
""")

st.divider()

col_wh_1, col_wh_2 = st.columns(2)
with col_wh_1:
    st.markdown("**Warehouse**")
with col_wh_2:
    st.selectbox("Warehouse",
                 (
                     "🏭 GA_RAW_WAREHOUSE_NEW", "🏭 GA_RAW_WAREHOUSE_OLD", " 🏭 MISC"
                 ), key="warehouse", label_visibility="hidden")


col_db_1, col_db_2 = st.columns(2)
with col_db_1:
    st.markdown("**Destination Database**")
with col_db_2:
    st.selectbox("Destination Database",
                 (
                     "💾 GA_RAW_DEST_DB", "💾 SOME_OTHER_DB", " 💾 YET_ANOTHER_DB"
                 ), key="database", label_visibility="hidden")


col_schema_1, col_schema_2 = st.columns(2)
with col_schema_1:
    st.markdown("**Destination Schema**")
with col_schema_2:
    st.selectbox("Destination Schema",
                 (
                     "📑 DEST_SCHEMA_NEW", "📑 DEST_SCHEMA_OLD", " 📑 OTHER"
                 ), key="schema", label_visibility="hidden")

col_role_1, col_role_2 = st.columns(2)
with col_role_1:
    st.markdown("**Role**", help="Role to be used for the connector.")
with col_role_2:
    st.selectbox("Role",
                 (
                     "👤 GA_RAW_RESOURCES_PROVIDER", "👤 GA_ANOTHER_PROVIDER", " 👤 SOME_ADDITIONAL_PROVIDER"
                 ), key="role", label_visibility="hidden")

st.divider()

col_bt_1, _, _, col_bt_4 = st.columns(4)

with col_bt_1:
    st.button("Back", key="back")

with col_bt_4:
    st.button("Configure", key="configure")

with st.sidebar:
    st.header("Configuration steps")
