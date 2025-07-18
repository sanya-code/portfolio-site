import streamlit as st
import base64

st.set_page_config(layout="wide")
st.title("Resume",anchor=False)
# Load resume
resume_path = "assets/resume.pdf"
with open(resume_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")

with open("assets/resume.pdf", "rb") as file:
    resume_bytes = file.read()
# Display a download button
st.download_button(
    label="📥 Download My Resume",
    data=resume_bytes,
    file_name="Sanya_Sharma_Resume.pdf",
    mime="application/pdf",
    help="Click to download my resume"
)

# Create viewer HTML
pdf_viewer = f"""
<style>
    .center-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 40px;
    }}

    .pdf-frame {{
        width: 60vw;  /* Adjust width as needed */
        height: 85vh;  /* Adjust height as needed */
        border: 1px solid #ddd;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }}

    .download-btn {{
        display: block;
        text-align: center;
        margin-top: 20px;
    }}

    .download-btn a {{
        padding: 10px 20px;
        background-color: #ffb6c1;
        color: black;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        border: none;
    }}

    .download-btn a:hover {{
        background-color: #ff9db1;
        color: white;
    }}
</style>

<div class="center-container">
    <iframe class="pdf-frame" src="data:application/pdf;base64,{base64_pdf}"></iframe>
</div>

"""

st.markdown(pdf_viewer, unsafe_allow_html=True)
