from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "302_TeamROG_Karl-Anthony Towns.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ayub Abdulkareem"
PAGE_ICON = ":wave:"
NAME = "Ayub Abdulkareem"
DESCRIPTION = """
Python Developer.
"""
EMAIL = "abdulkareemayub4619@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
    "Instagram":"https://instagram.com"
}
PROJECTS = {
    "🏆 scripting and scraping with python"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ expereince in object oriented programming
- ✔️ Strong experience and knowledge in Python and Excel
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Good communication skills
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python 
- 📊 Data Visulization
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("member of Zero to Mastery Bootcamp")

# --- JOB 1
st.write("🚧", "**Python Developer**")
st.write("09/2023 - Present")
st.write(
    """
- ► Used pycharm to display the movement pattern of group of individuals
- ► experience in testing computer programs
- ► designed data model using matplotlib
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("""
- ► An email checker
- ► A password generator
         """)
