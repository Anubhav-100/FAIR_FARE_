import streamlit as st
import streamlit.components.v1 as components
from navbar import render_navbar

def show():
    st.markdown("<h1>📞 Contact Us</h1>", unsafe_allow_html=True)

    # Read CSS content as a string
    with open("contact.css") as f:
        custom_css = f"<style>{f.read()}</style>"

    contact_html = f"""
    {custom_css}
    <div class="contact-section">
        <div class="profile-row">
            <img src="https://i.postimg.cc/Qt5b2ycb/IMG-20250724-090940.jpg" alt="Anubhav Photo" class="profile-img">
            <div class="profile-details">
                <h3>Anubhav Kumar Kesharwani</h3>
                <p class="role">Frontend Developer | UI Integrator</p>
                <p>Anubhav led the frontend design and backend implementation. He ensured smooth navigation, interactive UI, and responsive layouts for all pages.</p>
                <div class="contact-info">
                    <p>📞 [+91-6387399625]</p>
                    <p>📧 anubhavkesharwani38@gmail.com</p>
                    <p>🔗 
                        <a href="https://www.linkedin.com/in/anubhav-kesharwani-1a1267312" target="_blank" rel="noopener noreferrer">LinkedIn</a> | 
                        <a href="https://github.com/Anubhav-100" target="_blank" rel="noopener noreferrer">GitHub</a> | 
                        <a href="https://www.instagram.com/anubhav_k_47?igsh=MXFnd3F0cmlvc3ltYg==" target="_blank" rel="noopener noreferrer">Instagram</a> |
                    </p>
                </div>
            </div>
        </div>
        <div class="profile-row">
            <img src="https://i.postimg.cc/P5GZBz1k/Akshay2.jpg" alt="Akshay Photo" class="profile-img">
            <div class="profile-details">
                <h3>Akshay Goel</h3>
                <p class="role">Project Coordinator | Algorithm Architect | UI/UX Strategist</p>
                <p>Akshay handled project coordination, built the price comparison algorithm, and created the analytics dashboard in Power BI.</p>
                <div class="contact-info">
                    <p>📞 [+91-8923452712]</p>
                    <p>📧 workforgrad@gmail.com</p>
                    <p>🔗 
                        <a href="http://www.linkedin.com/in/akshaygoel16th" target="_blank rel="noopener noreferrer">LinkedIn</a> | 
                        <a href="https://github.com/akshayGoel16" target="_blank rel="noopener noreferrer">GitHub</a> | 
                        <a href="https://www.instagram.com/akshayofficial16" target="_blank rel="noopener noreferrer">Instagram</a> |
                    </p>
                </div>
            </div>
        </div>
        <div class="profile-row">
            <img src="https://i.postimg.cc/bYTBYr3M/Akash-2.jpg" alt="Akash Photo" class="profile-img">
            <div class="profile-details">
                <h3>Akash Soni</h3>
                <p class="role">Concept Designer | Prototype Developer</p>
                <p>Akash ideated the project and created the prototype. His early contributions helped shape the platform’s direction and scope.</p>
                <div class="contact-info">
                    <p>📞 [Your Number]</p>
                    <p>📧 your.email@example.com</p>
                    <p>🔗 
                        <a href="https://www.linkedin.com/in/akash-soni-52873a259" target="_blank rel="noopener noreferrer">LinkedIn</a> | 
                        <a href="https://github.com/AkashSoni-013" target="_blank rel="noopener noreferrer">GitHub</a> | 
                        <a href="https://www.instagram.com/just_aakash124" target="_blank rel="noopener noreferrer">Instagram</a> |
                    </p>
                </div>
            </div>
        </div>
    </div>
    """

    # Embed HTML + CSS directly in iframe
    components.html(contact_html, height=1400, scrolling=True)
