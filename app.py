import streamlit as st
import re

# Page configurations
st.set_page_config(page_title="PhishGuard Tool Security", page_icon="🛡", layout="centered")
st.title("🛡 PhishGuard: Cyber Safety Analyzer.")
st.write("Built by an ICS Student. Protect yourself from digital threats!")

menu = ["Home", "Password Checker", "Link Analyzer"]
choice = st.sidebar.selectbox("Select Security Tool", menu)

if choice == "Password Checker":
    st.subheader("🔑 Password Strength Analyzer")
    password = st.text_input("Enter a Password to test its security", type="password")
    
    if password:
        score = 0
        tips = []
        
        if len(password) >= 8:
            score += 1
        else:
            tips.append("Length should be at least 8 characters")
            
        if any(char.isdigit() for char in password):
            score += 1
        else:
            tips.append("Add at least one number to password (0-9)")
            
        if any(char.isupper() for char in password):
            score += 1
        else:
            tips.append("Add at least one uppercase letter to password (A-Z)")
            
        if any(char in "@#$%^&*()_+!=-[]{};:'/?.,<>~" for char in password):
            score += 1
        else:
            tips.append("Add at least one special character to password")
            
        # Display Results
        if score == 4:
            st.success("🔒 STRONG PASSWORD !")
        elif score == 3:
            st.warning("⚠ MEDIUM PASSWORD !")
        else:
            st.error("🚨 WEAK PASSWORD !")
            
        if tips:
            st.write("### Security Tips to Improve :")
            for tip in tips:
                st.write(f"- {tip}")

elif choice == "Link Analyzer":
    st.subheader("🌐 Phishing & False Link Analyzer")
    # FIX: type="url" ko hata kar simple rakha aur placeholder add kiya
    url = st.text_input("Paste a URL/Link to analyze :", placeholder="https://example.com")
    
    if url:
        st.write("Analyzing Link structure.....")
        is_suspicious = False
        reasons = []
        
        # 1. Keyword check
        suspicious_keywords = ["login", "bank", "secure", "update", "free", "verify", "gift", "facebook", "google-login"]
        if any(keyword in url.lower() for keyword in suspicious_keywords):
            is_suspicious = True
            reasons.append("Contains sensitive keywords often used by hackers to mimic real login pages")
            
        # 2. IP Address check (More strict pattern)
        if re.search(r'https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
            is_suspicious = True
            reasons.append("Uses a raw IP address instead of a secure domain name")
            
        # 3. URL Shortener check
        shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "t.co", "is.gd", "buff.ly"]
        if any(sch in url.lower() for sch in shorteners):
            is_suspicious = True
            reasons.append("Uses a URL shortener which can mask the final malicious destination.")
            
        # Final Output
        if is_suspicious:
            st.error("🚨 Suspicious Link! Be Careful before clicking this URL.")
            st.write("### Warnings found:")
            for reason in reasons:
                st.write(f"⚠ {reason}")
        else:
            st.success("✅ Looks Clean! No basic phishing indicators detected in the link syntax")

elif choice == "Home":
    st.write("### Welcome to PhishGuard !")
    st.write("This tool helps everyday users identify potential cyber risks in their passwords and the links they receive on WhatsApp or social media.")
