from pathlib import Path
import pandas as pd
import streamlit as st
from streamlit_player import st_player
from PIL import Image

paper_info = {'name':['THE WORST PART OF THE DAY: DAILY REFLECTIONS OF DEMENTIA FAMILY CAREGIVERS',
                      'Risk Factors of Cognitive Decline in Older Caregivers With HIV: An Emerging Hypothesis',
                      'Certified Nursing Assistants’ Perceived Workplace Violence in Long-Term Care Facilities: A Qualitative Analysis',
                      'Certified Nursing Assistants’ Experiences of Workplace Violence Caring for Persons With Dementia',
                      ],
              'publication':['Slack','Elsevier','Slack','Oxford University Press'],
              'journal':['Workplace Health & Safety','The Journal of the Association of Nurses in AIDS Care: JANAC','Workplace Health & Safety','Innovation in Aging'],
              'year':['2021','2021','2021','2020'],'role':['Author','Co-Author','Author','Author'],
              'Summary':['Family caregivers struggle with multi-dimensional demands in caring for persons living with dementia (PLWD). The challenges of caregiving combined with the requirements of daily life can impact the care of PLWD and the health and well-being of the caregivers. The purpose of this study was to describe caregivers’ perceptions of the worst part of their day in the context of daily caregiving challenges. Family caregivers completed online surveys reporting on various parts of their day. The survey included an optional open-ended question: “what was the worst part of your day?” Caregivers (N=165) completed diaries for 21 days resulting in 1,773 surveys that included a response to the optional open-ended question. A subset of data was analyzed using content analysis to identify initial codes and themes; further content analysis of the complete dataset was used to confirm and refine the identified codes and themes. Final analysis revealed 6 themes describing caregivers’ perceptions of the worst part of their day. These themes included days in which they had to: 1) cope with changes in their relationship with the PLWD, 2) manage their own health-related issues such as illness and lack of sleep, 3) struggle when there was a lack of help or support, 4) deal with daily life demands in the home along with the demands of caregiving, 5) cope with negative emotions such as sadness, grief, or anger over the disease process, 6) cope with physical exhaustion. The findings reflect daily stressors associated with caregiving for PLWD.',
                         'People with HIV (PWH) are living longer and healthier lives; thanks to combination antiretroviral therapy. As many PWH age, they find themselves providing care to family members and friends, just as their counterparts without HIV. The literature indicates that becoming a caregiver creates conditions that compromise one cognitive function. Additionally, nearly 45% of all PWH experience HIV-associated neurocognitive disorder and are already vulnerable to cognitive impairment due to HIV, aging, and accompanying health conditions, and lifestyle factors. Given what is known, we assert that caregivers with HIV, especially as they age, are at additional risk for developing cognitive impairments. The purpose of this commentary was to briefly examine the juxtaposition between cognitive vulnerability of caregiving and the cognitive vulnerability of aging with HIV. Potential factors contributing to impaired cognition include stress, lack of social support, stigma, lifestyle, and comorbidities. Implications for clinical practice and research are provided.',
                         'Background Certified nursing assistants (CNAs) provide 80% to 90% of direct care and are 23 times more likely to experience aggressive behavior from residents in long-term care (LTC) facilities than in other health care settings. The purpose of this study was to describe CNAs’ perceptions of workplace violence while working in LTC facilities. Methods Ten CNAs were recruited from five LTC facilities through snowball sampling. A semi-structured interview was conducted with CNAs currently working in LTC facilities in Alabama. Question domains included (a) demographics, (b) residents’ behavior, (c) behavior of residents with dementia, (d) experiences of verbal or physical violence from residents, (e) quality of care delivered, (f) coping strategies, (g) administrative support, and (h) training for dementia-related care challenges. The resulting transcripts were thematically analyzed. Findings CNAs described workplace violence as part of the job. They expressed a lack of administrative support as inadequate communication and a dismissal of violence against them. They regularly experienced racially charged abuse, but the perception of abuse was moderated by the presence or absence of dementia. They described a lack of training and direction to recognize and de-escalate workplace violence. Conclusions/Application to Practice Workplace violence from residents residing in LTC facilities is an occupational health risk for CNAs. LTC facilities need a multisystem approach to reduce episodes of resident-on-CNA violence. This approach should include comprehensive training to recognize triggers of violent behavior, especially when working with individuals with dementia, as well as administrative support, and mental health resources to address the cumulative and negative consequences of racism.',
                         'Problem: Certified nursing assistants (CNAs) are the primary providers of direct care to persons residing in long term care facilities (LTCFs), many of whom have dementia. The need to deliver direct and intimate care increases CNAs’ exposure to verbal and physical workplace violence. Purpose: To describe CNAs’ experiences of physical and verbal workplace violence experienced during direct care activities in LTCFs. Design: Qualitative. Sample & Procedure: Ten African-American CNAs (9 female, 1 male) were recruited using snowball sampling from multiple LTCFs. Interviews were recorded and transcribed. NVivo12 software was used to manage the thematic analyses. Results: The identified themes were: 1) CNAs’ perception that verbal and physical abuse was “part of the job” and unavoidable; 2) CNAs’ feelings of minimization of the abuse by administration; and 3) inadequate CNA training to recognize and de-escalate triggers of verbal and physical violence, notably care-resistant behavior. Conclusion: The combination of institutional tolerance of workplace violence, coupled with CNAs’ insufficient training in de-escalating volatile interactions with cognitively-impaired residents, is creating an unfavorable, possibly dangerous, workplace environment for CNAs. Implications: As more states elevate assaults on healthcare workers to felony crimes, there is an emerging risk of criminalizing dementia-related behavior in an attempt to address workplace violence. Interventions focused on helping CNAs recognize and de-escalate care-resistant behavior are necessary for violence prevention programs in LTCFs. Limitations: CNAs may have self-censored and under-described the severity of their experiences during face-to-face interviews, even with confidentiality protocols and the practice of off-site interviews.'
                         ],
                         'file':['1.pdf',
                                 'Vanceetal2022.Cognitive_Decline_in_CGwithHIV.JANAC1.pdf',
                                  'CertifiedNursingAssistantsPerceivedWorkplaceViolenceinLong.pdf',
                                 'Certified_Nursing_Assistants_Experiences_of_Workp.pdf'],
                         'images':{'0':[{'path':'images/rpa1.PNG','caption':'Digitization pipeline','width':600}],
                                  '1':[[{'path':'images/pr1.PNG','caption':'Capture seed words'},{'path':'images/pr2.PNG','caption':'cluster words using seed words'},{'path':'images/pr3.PNG','caption':'clean junk words'}],
                                                                                                                                                                                                                            [{'path':'images/hw1.PNG','caption':'Filter 1'},
                                                                                                                                                                                                                                                                                                                                                                                                                    {'path':'images/hw2.PNG','caption':'Filter 2'},{'path':'images/hw3.PNG','caption':'Filter 3'}]]}}

rpa_metrics = pd.DataFrame([['Overall',66.4, 72.5],['printed rx',54.6, 64.6],['handwritten',67.3,73.3]], columns=['category','ds','non-ds'])
rapid_metrics = pd.DataFrame([['printed',91.6,70,79.4],['handwritten',21.1,34.7,26.2],['Brute-Force_Printed',29.9,82.7,41.8],['Brute-Force_Handwritten',0.2,62,0.3]],columns=['category','precision','recall','f1_score'])
rapid_metrics = rapid_metrics.set_index(['category'])
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
    "Facebook": "https://github.com",
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
st.subheader("BOARD CERTIFICATION")

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
st.subheader("Education")           

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
st.subheader("AWARDS/HONORS")              


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

st.subheader('JOURNAL REVIEW ACTIVITY')

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

st.subheader('PROFESSIONAL SOCIETIES 📝')

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

st.subheader('Research Papers 📝')


def paper_summary(index):
    st.markdown('📃<em><strong>'+paper_info['name'][index]+'</strong></em>',unsafe_allow_html=True)
    st.caption(paper_info['role'][index])
    st.caption(paper_info['journal'][index]+' , '+paper_info['publication'][index]+' , '+paper_info['year'][index])
    with st.expander('>'+'Abstract:'):
        with st.spinner(text="Loading details..."):
                st.write('>'+paper_info['Summary'][index])
                pdfFileObj = open('{}'.format(paper_info['file'][index]), 'rb')
              
                
                st.download_button('download paper',pdfFileObj,file_name=paper_info['file'][index],mime='pdf')
    


paper_summary(0)
paper_summary(1)
paper_summary(2)
paper_summary(3)

st_player("https://www.facebook.com/watch/?v=199533675658464")



