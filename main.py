import streamlit as st 


about_page = st.Page(
    page="views/about.py",
    title="About Me",
    default = True,
    icon="🎀"
    
)
projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon="📂"
)

writing_page = st.Page(
    page="views/my_work.py",
    title="Writing",
    icon="🖊️"
)
design_page = st.Page(
    page="views/design.py",
    title="Designing",
    icon="🍡"
)
experience_page = st.Page(
    page="views/exp.py",
    title="Experience",
    icon="📈"
)
resume_page = st.Page(
    page="views/resume.py",
    title="Resume",
    icon="📃"
)

pg = st.navigation(
    {
        "Info":[about_page,experience_page,resume_page,projects_page],
        "More than Just Tech":[writing_page, design_page]
    }
    
    )

pg.run()