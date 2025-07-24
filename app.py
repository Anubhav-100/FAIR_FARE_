import streamlit as st
import os
from navbar import render_navbar
import Home, About, Dashboard, Contact

# Page Config
st.set_page_config(page_title="Fair_Fare", layout="wide", initial_sidebar_state="collapsed")

# Load CSS
for css_file in ["style.css", "sbackground.css", "navbar.css", "content.css"]:
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render HTML Navbar (header)
navbar_html = render_navbar()
if not navbar_html:
    navbar_html = "<nav><!-- Default navbar --></nav>"
st.markdown(navbar_html, unsafe_allow_html=True)


# --- Get and clean the page param
raw_page = st.query_params.get("page", "Home")
page = raw_page[0] if isinstance(raw_page, list) else raw_page
page = page.capitalize()  # convert to "Home", "Dashboard", etc.

# --- Routing
if page == "Home":
    Home.show()
elif page == "Dashboard":
    Dashboard.show()
elif page == "About":
    About.show()
elif page == "Contact":
    Contact.show()
else:
    st.error("Page not found")

