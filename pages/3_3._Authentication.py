import streamlit as st

st.set_page_config(layout="centered")

st.header("Authenticate to Google Cloud Platform")

st.markdown("""
To connect to Google Cloud Platform choose the authentication method and provide relevant credentials.
After that, you will be redirected to the Google Cloud Provider sign-in page. 
Make sure that your browser is not blocking pop-ups for this site.
Note that OAuth2 requires configuring an application registry in Google Cloud Platform. [Learn More](#)
""")

st.divider()

st.radio("Authentication method",
         ("Basic (recommended) - The whole database will be automatically replicated and incur costs when there "
          "is a consumer demand in a selected region",
          "oAuth - To fullfill requests, you must manually set up accounts in visible regions, manually replicate "
          "databaases to each account, create secure shares in each account, and attach those shares to "
          "this listing"), key="auth_method", label_visibility="hidden")

st.divider()

col_redirect_1, col_redirect_2 = st.columns([1, 2])
with col_redirect_1:
    st.markdown("**Redirect URL**")

with col_redirect_2:
    st.code("https://<org_name>-<account_name>.apps...")

col_client_id_1, col_client_id_2 = st.columns([1, 2])
with col_client_id_1:
    st.markdown("**Client ID**", help="Client ID for the application.")

with col_client_id_2:
    st.text_input("Client ID", value="f921cea18ed78910e25e5a9fb9aeee56a", key="client_id", label_visibility="hidden")

col_client_secret_1, col_client_secret_2 = st.columns([1, 2])
with col_client_secret_1:
    st.markdown("**Client Secret**", help="Client Secret for the application.")

with col_client_secret_2:
    st.text_input("Client Secret", value="f921cea18ed78910e25e5a9fb9aeee56a", key="client_secret",
                  label_visibility="hidden")

st.divider()

st.markdown("A secret object will be created to securely store the access and refresh "
            "token from Google Cloud Platform.")

col_secret_name_1, col_secret_name_2 = st.columns([1, 2])
with col_secret_name_1:
    st.markdown("**Secret Name**", help="Name of the secret object to be created.")

with col_secret_name_2:
    st.text_input("Secret Name", value="connectors_ui.googlecloudplatform_GZBZGD...", key="secret_name", disabled=True,
                  label_visibility="hidden")

st.divider()

col_bt_1, _, _, col_bt_4 = st.columns(4)

with col_bt_1:
    st.button("Back", key="back")

with col_bt_4:
    st.button("Authenticate", key="authenticate")

with st.sidebar:
    st.header("Configuration steps")
