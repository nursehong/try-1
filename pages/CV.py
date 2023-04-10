from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent  if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | ChunHong Xiao"
PAGE_ICON = ":wave:"
NAME = "ChunHong Xiao"
DESCRIPTION = """
Ph.D.  Geriatric Nursing Rearcher.My research is focused on the interaction of behavioral symptoms of dementia and the social, care, and physical environment. 
"""
EMAIL = "dehong@uab.edu"
SOCIAL_MEDIA = {
    "ResearchGate": "https://www.researchgate.net/profile/Chunhong-Xiao",
    "LinkedIn": "https://www.linkedin.com/in/chunhong-xiao-5a8299b3/",
    "FaceBook": "https://github.com",
    "Twitter": "https://twitter.com/ChunhongXiao",
}
PROJECTS = {
    "🏆 Hazard objects detecting in people living with dementia": "https://",
    "🏆 Nursing Documents analysis": "https://",
    "🏆 Good or Bad day - measuring people living with dementia's situation": "https://",
    "🏆 GBTM in Nursing Research": "https://",
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

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ focusing on the variability of behavioral symptoms of dementia, the trajectories of care-resistant behavior and their impact on oral health outcomes among persons with dementia in long-term care facilities
- ✔️ Strong hands on experience and knowledge in Deep Learning
- ✔️ Good understanding of Geriatric Nurse principles and their respective applications
- ✔️ Alabama #1-177126 (RN) 
"""
)

st.markdown('''
### BOARD CERTIFICATION
''')

txt('**Diversity, Equity, and Inclusion Training Courses** , *University of Alabama at Birmingham*, U.S.A.',
'2021-Present')
txt('**Basic Life Support** , *American Heart Association*, U.S.A.',
'2019-Present')


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")

st.markdown('''
- 👩‍💻 Nursing:
  - Geriatric Nursing 
  - Alzheimer's Disease and Related Dementia behavioral symptoms
  - Dementia caregiving
  -Care coordination for caring for persons living with dementia.
  - Dementia-related challenging behavior, specifically care-resistant behaviors.
  - Neuropsychology
  - Workplace health and safety Dementia Care · Geriatric Nursing · Oral health · Global Nursing
- 👩‍💻 Programming:       Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling:          Group based trajectory modeling · Logistic regression · linear regression · decition trees
- 🗄️ Databases:         Stata,Postgres, MongoDB, MySQL
'''
)
st.markdown('''
### Education
''')
txt('**Post- Doc Fellow** (Nursing ), *University of Alabama at Birmingham*, U.S.A.',
'2023-present')
st.markdown('''
- Project: DRDB
  Dr. Pickering Lab
''')


txt('**Doctor of Philosophy** (Nursing ), *University of Alabama at Birmingham*, U.S.A.',
'2019-2022')
st.markdown('''
- GPA: `3.89`
- Research thesis entitled `Care-resistant Behavior Trajectories of Persons Living with Dementia in Nursing Homes and Distal Outcomes in Oral Health: A Secondary Analysis. 
  Chair: 
  Dr. Rita A Jablonski  
''')

txt('**Bachelors of Science** (Nursing),  *University of Alabama at Birmingham*, U.S.A.',
'2015-2019')
st.markdown('''
- GPA: `3.99`
- Graduated in Honor Program.
''')
            
st.markdown('''
## AWARDS/HONORS
''')

txt('- *Award during 2022 PHD intensive: Core Value Award for “Integrity”* ','2022')

txt('- *Award during 2022 PHD intensive: Core Value Award for “Communication”* ','2022')

txt('- *The Lowder Travel Award* ','2021')

txt('- *3MT (3 Minute Thesis) Finalist, UAB Graduate School* ','2021')

txt('- *Best Overall Poster --1st Annual DNP/PhD Scholarship Collaborative* ','2021')
 
txt('- *Published article, Xiao (2021) selected by the editor of Workplace Health &Safety to present as the best article of the year in the International Academy of Nursing Editors (INANE) 2021 conference”* ','2021')

txt('- *Award during 2021 PHD intensive: Core Value Award for “Caring"* ','2021')

txt('- *Award during 2021 PHD intensive: Core Value Award for “Integrity”* ','2021')

txt('- *SNRS Research Highlight--Brain and Alzheimer’s Awareness Month* ','2021')

txt('- *Award during 2022 PHD intensive: Core Value Award for “Communication”* ','2022')

txt('- *Honored to nominate Graduate Dean Excellence in Mentorship Award for Dr. Ada Markaki (Award Received)* ','2021')

txt('- *Graduate Research Assistantship* ','2021-Present ')

txt('- *UAB Blazer Fellowship* ','2019-2020')
 
txt('- *UAB School of Nursing Outstanding Nursing Honors Students* ','2019')

txt('- *Graduate with honor of Cum Laude "* ','2019')

txt('- *Completed the UABSON Honors Program* ','2019')


txt('- *UAB Student Nurses’ Association Funding Award for National Conference* ','2019')

txt('- *Phi Kappa Phi, National Honor Society for All Academic Disciplines* ','2018')

txt('- *Sigma Theta Tau International Honor Society of Nursing, Nu Chapter* ','2018')
 
txt('- *Dean List for Two Semesters at the University of Alabama* ','2015-2016 ')


st.markdown('''
## JOURNAL REVIEW ACTIVITY
''')

txt('- **BMC Nursing** ','2023-Present ')

txt('- **Journal of International Medical Research** ','2023-Present ')

txt('- **Research in Gerontological Nursing** ','2021')



# --- WORK HISTORY ---
st.write('\n')
st.subheader("GRANT SUPPORT")
st.write("---")

# --- JOB 1
st.write("🚧", "**American Alzheimer’s Association Research Fellow Grant (LOI submitted)**")
st.write("2023")
st.write("""
- **`Number:`** 
""")
st.write("""
- **`Agency:`** American Alzheimer’s Association 
""")
st.write("""
- **`Amount:`** 
""")

st.write("""
- **`PI:`** Chunhong Xiao  
--`Mentor:` Dr. Carolyn Pickering   	
""")

# --- JOB 1
st.write("🚧", "**Testing Dementia Caregiver TeleCoaching to Reduce Episodes of Abuse and Neglect by Recognizing and Managing Care-Resistant Behaviors**")
st.write("02/2020 - Present")
st.write("""
- **`Number:`** R01AG074255
""")
st.write("""
- **`Agency:`** National Institute on Aging/NIH 
""")
st.write("""
- **`Amount:`** 690729.00
""")

st.write("""
- **`PI:`** Rita A Jablonski	
""")
 # ---        
st.write("🚧", "**DSDS Discovery Solution for Dementia Symptoms **")
st.write("02/2020 - Present")
st.write("""
- **`Number:`** R01AG060083
""")
st.write("""
- **`Agency:`** National Institute on Aging/NIH 
""")
st.write("""
- **`Amount:`** 2.87 million
""")

st.write("""
- **`PI:`** Carolyn E Ziminski Pickering	
""")

 # ---        
st.write("🚧", "**Brush Away Infection  **")
st.write("02/2020 - Present")
st.write("""
- **`Number:`** C90629769
""")
st.write("""
- **`Agency:`** Alabama Department of Public Health & Alabama Medicaid Agency 
""")
st.write("""
- **`Amount:`**  2.3 million
""")

st.write("""
- **`PI:`** Rita A Jablonski	
""")     


st.markdown('''
## PROFESSIONAL SOCIETIES:
''')
st.write("""**Southern Nursing Research Society**  """ )
txt('- Member','2023- Present ')


st.write("""**Sigma Global Leadership Mentoring Community**  """ )
txt('- Mentee','2022- Present ')


st.write("""**GNSA (The Graduate Nursing Student Academy)**  """ )
txt('- Member /Senator ','2021- Present ')

st.write("""**Sigma Theta Tau International Honor Society of Nursing**  """ )
txt('- Member','2018- Present ')


st.write("""**Nu-Large Chapter of Sigma Leadership Board**  """ )
txt('- Governance ','2021- Present ')


st.write("""**Gerontological Society of America (GSA)**  """ )
txt('- Member','2020- Present ')


st.write("""**Gerontological Society of America (GSA)**  """ )
txt('- Conference Abstract Reviewers ','2021-2022 ')




