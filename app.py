from pathlib import Path


import streamlit as st
from PIL import Image

#--- PATH SETTINGS ---
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = curr_dir / "styles" / "main.css" 
resume_file = curr_dir / "assets" /"armanres.pdf"
profile_pic = curr_dir / "assets" /"pfp.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Armaan Poonawalla"
PAGE_ICON = ":wave:"
NAME = "Armaan Murad Poonawalla"
DESCRIPTION = """ I am a hard-working individual with a passion to use my educational and life skills to contribute significantly to
their growth. I believe in being 100% committed to any company I work for and to look after its interests."""

EMAIL = "armaanamp@gmail.com"
SOCIAL_MEDIA = {"Instagram" : "https://www.instagram.com/armaanamp/", 
                "LinkedIn" : "www.linkedin.com/in/armaanpoonawalla"}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PFP ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file, "rb")as pdf_file:
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
        label ="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    
    st.write("📧", EMAIL)
        
# --- SOCIAL LINKS ---
st.subheader("👇 Connect with Me ")
cols = st.columns(len(SOCIAL_MEDIA))

# Loop through each platform and URL, creating a clickable link in each column
for i, (platform, url) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f"[{platform}](link)")
    
# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - 🗸Currently pursuing a Computer Science degree at MacEwan University with a Dean's Scholarship.
    - 🗸 Employed as a Gameday and Events Retail Associate at Compass Group Canada, providing guest interaction and maintaining a professional retail environment.
    - 🗸 Long-term volunteer at Ismaili Jamatkhana, assisting seniors and children, setting up halls, organizing activities, and teaching kindergarteners about Islam.
    - 🗸 Volunteered with the African Community in St. Albert, assisting in fundraising events and venue setup.
    - 🗸 Engaged with children aged 7-14 as a volunteer in summer camps, demonstrating leadership and organizational skills.
""")

# --- SKILLS ---
st.write("#")
st.subheader('Hard skills')
st.write(
    """
    - Programming: Python
    - Strong analytical, problem-solving, and critical thinking skills.
    - Experienced in customer service and retail
    - Demonstrated leadership and organizational skills
    """)


# --- WORK HISTORY ---
st.write("#")
st.subheader('Work History')
st.write("---")

# --- JOB 1 ---
st.write ("**Gameday and Events Retail Sales Associate**")
st.write("04/2024 - Present")
st.write(
    """
   - Communicate and interact with guests to provide an enjoyable shopping experience.
- Provide knowledge and recommendations based on guest feedback and inquires.
- Represent the brand by creating a warm and welcoming retail environment
- Maintain sales floor and/stockroom detailed merchandising standards
- Uphold the highest level of professionalism and customer service to ensure both the Compass and team/arena
brand are represented positively""")




