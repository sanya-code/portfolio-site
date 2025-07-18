import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_pic.jpg",width=250)

with col2:
    st.title("Hi, I'm Sanya!",anchor=False)
    st.write(' ***“Combining Art and Data into meaningful visualisations”*** ')
    st.write("For Queries:")

    # st.markdown("""
    #     <a href="https://www.linkedin.com/in/sanya-sharma-866805242/" target="_blank">
    #         <button style='background-color: #a94064; color: white; padding: 0.5em 1em; border: none; border-radius: 5px;'>
    #             🔗 Connect with me on LinkedIn
    #         </button>
    #     </a>
    # """, unsafe_allow_html=True)

    if st.button("✉️ Contact Me"):
        show_contact_form()



    linkedin_url = "https://www.linkedin.com/in/sanya-sharma-866805242/"  # Replace with your actual LinkedIn URL

    
    st.markdown("""
        <a href="https://www.linkedin.com/in/sanya-sharma-866805242/" target="_blank">
            <button style="padding: 0.5rem 1rem; font-size: 1rem; border: none; background-color: #a94064; color: white; border-radius: 5px; cursor: pointer;">
                🔗 Connect on LinkedIn
            </button>
        </a>
    """, unsafe_allow_html=True)




st.divider()

st.subheader("🪄 About Me",anchor=False)
st.markdown("""
I'm **Sanya Sharma**, a Creative Technologist currently pursuing my **Master’s in Computer Applications**.  
With a deep interest in design, storytelling, and tech, I love building experiences that are both beautiful and functional. From crafting **aesthetic websites** to exploring **data and AI**, I bridge the gap between logic and emotion through code.
""")

st.divider()

st.markdown("## 🧠 My Skills")

# Create two columns: Hard Skills (left), Soft Skills & Interests (right)
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown("### 🔧 Hard Skills")
    hard_skills = [
        "HTML/CSS", "Tailwind CSS", "Python", "Streamlit", "Electron JS",
        "MySQL", "Git/GitHub", "Data Structures and Algorithms",
        "Data Analysis", "Pandas", "Numpy", "MS Office",
        "UI-UX Designing", "Figma", "Graphic Designing", "Content Writing"
    ]

    # Display hard skills as bullet list in two-column layout
    for i in range(0, len(hard_skills), 2):
        col1, col2 = st.columns(2)
        col1.markdown(f"- {hard_skills[i]}")
        if i + 1 < len(hard_skills):
            col2.markdown(f"- {hard_skills[i+1]}")

with right_col:
    st.markdown("### 🌸 Soft Skills")
    soft_skills = [
        "Problem Solving",
        "Time Management",
        "Open Communication"
    ]
    for skill in soft_skills:
        st.markdown(f"- {skill}")

    

# Create 3 descriptive columns
    st.markdown("### 🎯 Interests")

    # Create 2 descriptive columns
    interest_col1, interest_col2 = st.columns(2)

    with interest_col1:
        st.markdown("- 📚 Reading")
        st.markdown("- ✍️ Writing")
        st.markdown("- 🌍 Traveling")

    with interest_col2:
        st.markdown("- 🎤 Open-Mics")
        st.markdown("- 📰 Journalism")
        st.markdown("- 🧶 Crochet")





st.divider()


st.markdown("## 🎓 Education")

st.markdown("#### 🧠 Guru Gobind Singh Indraprastha Univeristy *(2024–2026)*")
st.markdown("""
- **Master of Computer Applications (MCA)**  
- **CGPA**: 9.37
""")



st.markdown("#### 💻 G.D Goenka University, Gurugram *(2021–2024)*")
st.markdown("""
- **Bachelor of Computer Applications (BCA)**  
- **CGPA**: 9.10
""")

st.markdown("#### 🏫 Amity International School, Sec 43 *(2010–2021)*")
st.markdown("""
- **12th – Humanities + Information Practices**: 91%  
- **10th**: 76%
""")

st.divider()


st.markdown("### 💫 Wait up, There's more!")

sec1,sec2,sec3 = st.columns(3, vertical_alignment="center", gap="small")

with sec1:
    st.markdown("#### Find my work experience here")
    if st.button("Experience"):
        st.switch_page("./views/exp.py")
with sec2:
    st.markdown("#### Find my resume here")
    if st.button("Resume"):
        st.switch_page("./views/resume.py")
with sec3:
    st.markdown("#### Who said tech people can't have more hobbies?")
    if st.button("Writing"):
        st.switch_page("./views/my_work.py")

    if st.button("Design"):
        st.switch_page("./views/design.py")



