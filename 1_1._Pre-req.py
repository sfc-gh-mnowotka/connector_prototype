import streamlit as st

st.set_page_config(layout="centered")

TOTAL_STAGES = 3

if "stages_completed" not in st.session_state:
    st.session_state["stages_completed"] = 0
if "cdp_completed" not in st.session_state:
    st.session_state["cdp_completed"] = False
if "bq_completed" not in st.session_state:
    st.session_state["bq_completed"] = False
if "ga_completed" not in st.session_state:
    st.session_state["ga_completed"] = False

stages_completed = st.session_state["stages_completed"]

col_top_1, col_top_2 = st.columns([9, 1])

with col_top_1:
    st.header("Required actions before configuration")
with col_top_2:
    st.button(f"{stages_completed}/{TOTAL_STAGES}", disabled=True)

st.markdown("""
In order to fully complete the Connector configuration, you must meet a few requirements. **You may need help other people to fully configure Connector.**.
When you have completed a step, click Mark task done to move on. [Learn More](#)
""")

st.divider()

col_cdp_1, col_cdp_2 = st.columns([2, 1])
with col_cdp_1:
    st.subheader("Check Google Cloud Platform in BigQuery")

with col_cdp_2:
    cdp_completed = st.session_state["cdp_completed"]
    label = "✔️ Mark task as done" if not cdp_completed else "Done!"
    if st.button(label, key="cdp", disabled=cdp_completed):
        st.session_state["cdp_completed"] = True
        st.session_state["stages_completed"] += 1
        st.experimental_rerun()

st.markdown("""
Check GCP project in BigQuery Instance. Tick the checkbox when done.
""")

col_cdp_docs_1, col_cdp_docs_2, col_cdp_docs_3 = st.columns(3)
with col_cdp_docs_1:
    st.markdown("[📘 Read tutorial](#)")
with col_cdp_docs_2:
    st.markdown("[🔗 Documentation](#)")
with col_cdp_docs_3:
    st.markdown("[⬇️ Guide_GCP_project.pdf](#)")

st.divider()

col_bq_1, col_bq_2 = st.columns([2, 1])
with col_bq_1:
    st.subheader("Check that you have access to this BigQuery")

with col_bq_2:
    bq_completed = st.session_state["bq_completed"]
    label = "✔️ Mark task as done" if not bq_completed else "Done!"
    if st.button(label, key="bq", disabled=bq_completed):
        st.session_state["bq_completed"] = True
        st.session_state["stages_completed"] += 1
        st.experimental_rerun()

st.markdown("""
Check GCP project in BigQuery Instance. Tick the checkbox when done.
""")

col_bq_docs_1, col_bq_docs_2, col_bq_docs_3 = st.columns(3)
with col_bq_docs_1:
    st.markdown("[📘 Read tutorial](#)")
with col_bq_docs_2:
    st.markdown("[🔗 Documentation](#)")
with col_bq_docs_3:
    st.markdown("[⬇️ Guide_BQ_access.pdf](#)")

st.divider()

col_ga_1, col_ga_2 = st.columns([2, 1])
with col_ga_1:
    st.subheader("Check that you have linked Google Analytics with BigQuery")

with col_ga_2:
    ga_completed = st.session_state["ga_completed"]
    label = "✔️ Mark task as done" if not ga_completed else "Done!"
    if st.button(label, key="ga", disabled=ga_completed):
        st.session_state["ga_completed"] = True
        st.session_state["stages_completed"] += 1
        st.experimental_rerun()

st.markdown("""
Check GCP project in BigQuery Instance. Tick the checkbox when done.
""")

col_ga_docs_1, col_ga_docs_2, col_ga_docs_3 = st.columns(3)
with col_ga_docs_1:
    st.markdown("[📘 Read tutorial](#)")
with col_ga_docs_2:
    st.markdown("[🔗 Documentation](#)")
with col_ga_docs_3:
    st.markdown("[⬇️ Guide_links_GAandBQ.pdf](#)")

st.divider()

col_bt_1, _, col_bt_3, col_bt_4 = st.columns(4)

with col_bt_1:
    if st.button("Cancel", key="cancel"):
        st.session_state["cdp_completed"] = False
        st.session_state["bq_completed"] = False
        st.session_state["ga_completed"] = False
        st.session_state["stages_completed"] = 0
        st.experimental_rerun()


with col_bt_3:
    if st.button("Mark all as done", key="all_done"):
        st.session_state["cdp_completed"] = True
        st.session_state["bq_completed"] = True
        st.session_state["ga_completed"] = True
        st.session_state["stages_completed"] = TOTAL_STAGES
        st.experimental_rerun()

with col_bt_4:
    st.button("Start configure", key="start", disabled=st.session_state["stages_completed"] != TOTAL_STAGES)

with st.sidebar:
    st.header("Configuration steps")



