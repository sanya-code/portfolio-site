import streamlit as st
import base64

st.set_page_config(layout="wide")
st.title("📃 Resume", anchor=False)

st.divider()
# Path to the resume PDF
pdf_path = "assets/resume.pdf"

# Read PDF file as binary
with open(pdf_path, "rb") as file:
    pdf_bytes = file.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")  # encode for embedding

# Download button
st.download_button(
    label="📥 Download My Resume",
    data=pdf_bytes,  # not the path, the actual file content
    file_name="Sanya_Sharma_Resume.pdf",
    mime="application/pdf",
    help="Click to download my resume"
)



# Show the resume image
image_path = "assets/resumeimg.png"
st.image(image_path, use_container_width=True)
