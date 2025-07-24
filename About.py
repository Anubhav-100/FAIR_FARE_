import streamlit as st
from navbar import render_navbar
import streamlit.components.v1 as components

def show():
    # Your page content
    st.markdown("<h1>📘 About Fair_Fare</h1>", unsafe_allow_html=True)

    # ABOUT CONTENT
    about_html = """
    <div style="padding: 2.5rem; background-color: rgba(255,255,255,0.92); border-radius: 15px; box-shadow: 0 0 15px rgba(0,0,0,0.1);">
    
        <h1 style="color: #222222; font-size: 3rem; font-weight: 800; margin-bottom: 1.5rem;">📘 About This App</h1>
    
        <p style="font-size: 1.6rem; line-height: 2; color: #222; margin-bottom: 2rem;">
            Welcome to <strong>FairFare App</strong> – your one-stop dashboard for exploring and analyzing ride fare patterns in a visually engaging way! 🚖📊<br>
            This app is built using <strong>Streamlit</strong> to deliver a clean, interactive, and responsive interface for users to analyze taxi/ride data, visualize trends, and draw meaningful insights using charts and maps.
        </p>

        <h2 style="font-size: 2.2rem; color: #111; margin-top: 2.5rem;">✨ Key Features</h2>
        <ul style="line-height: 2; font-size: 1.5rem; color: #333; margin-left: 1.5rem; margin-bottom: 2rem;">
            <li>📍 Compare fares between <strong>Ola, Uber,</strong> and <strong>Rapido</strong> for your selected route.</li>
            <li>🚘 Get real-time estimation for <strong>Hatchback, SUV,</strong> and <Strong>Sedan</strong> ride types.</li>
            <li>📊 Visualize price comparisons with intuitive charts and metrics.</li>
            <li>📦 Download estimated fares as <strong>PDF</strong> or <strong>CSV</strong> for future reference.</li>
            <li>⚡ Designed with a fast and interactive interface using <strong>Streamlit</strong>.</li>
        </ul>

        <h2 style="font-size: 2.2rem; color: #111; margin-top: 2.5rem;">🧠 Tech Stack</h2>
        <ul style="line-height: 2; font-size: 1.5rem; color: #333; margin-left: 1.5rem; margin-bottom: 2rem;">
            <li>🧩 <strong>Streamlit</strong> – for app framework and UI rendering</li>
            <li>🎨 <strong>HTML + CSS</strong> – for custom styling and responsive navbar</li>
            <li>📊 <strong>Power BI</strong> – for interactive data visualization</li>
            <li>📁 <strong>Pandas</strong> – for data manipulation and filtering</li>
        </ul>

        <h2 style="font-size: 2.2rem; color: #111; margin-top: 2.5rem;">👨‍💻 Developer Note</h2>
        <p style="font-size: 1.55rem; line-height: 2; color: #222; margin-bottom: 2rem;">
            This project was developed with love, code, and a whole lot of debugging! ❤️🛠️<br>
            The goal is to showcase data analytics using a real-world use case and offer an intuitive tool for exploring ride fare trends.<br>
            Whether you're a data analyst, a student, or just curious — dive in and explore!
        </p>

        <p style="margin-top: 2rem; font-size: 1.4rem; color: #666; font-style: italic;">
            — Built by Anubhav 🚀
        </p>

    </div>
    """

    components.html(about_html, height=900, scrolling=True)