import streamlit as st
from streamlit.components.v1 import html

# Set page config
st.set_page_config(
    page_title="Jerim Owino - AI/ML Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default styling
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}
[data-testid="stToolbar"] {display: none;}
.reportview-container {
    margin-top: -2em;
}
#root > div:nth-child(1) > div > div > div > div > section > div {
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read portfolio HTML
with open('portfolio.html', 'r', encoding='utf-8') as f:
    portfolio_html = f.read()

# Display portfolio
html(portfolio_html, width=None, height=10000, scrolling=True)
