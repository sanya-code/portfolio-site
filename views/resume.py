import streamlit as st
import base64

st.set_page_config(layout="wide")
st.title("Resume", anchor=False)

# Load resume image (for download and display)
image_path = "assets/resumeimg.png"

with open(image_path, "rb") as file:
    image_bytes = file.read()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

# Download button
st.download_button(
    label="📥 Download My Resume",
    data=image_bytes,
    file_name="Sanya_Sharma_Resume.png",
    mime="image/png",
    help="Click to download my resume as an image"
)

# Display image using HTML and base64
st.markdown(f"""
    <style>
        .image-container {{
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }}

        .resume-image {{
            max-width: 70%;
            border: 1px solid #ddd;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }}
    </style>

    <div class="image-container">
        <img class="resume-image" src="data:image/png;base64,{base64_image}" alt="Resume Image">
    </div>
""", unsafe_allow_html=True)
