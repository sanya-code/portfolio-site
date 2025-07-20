import streamlit as st

st.set_page_config(layout="wide")
st.title("📁 Projects", anchor=False)

st.markdown("---")

# Project 1
st.markdown("""
### 🤘 Sign Language Prediction Model  
**🧰 Tech Stack:** Python, TensorFlow/Keras, OpenCV, NumPy, Matplotlib, Pandas

- Developed a CNN-based deep learning model to classify American Sign Language (ASL) alphabets from RGB images using TensorFlow and Keras.  
- Trained on a labeled image dataset and saved the model in .h5 format for deployment or further use.                                     
- Designed a modular and scalable codebase with separate modules for data loading, preprocessing, model architecture, training, and evaluation

🔗 [GitHub Repo](https://github.com/sanya-code/Sign-Language-Prediction-Model)
""")

st.divider()

# Project 2
st.markdown("""
### 🗃️ Portfolio Website
**🧰 Tech Stack:** HTML, CSS, Streamlit, SMTP

- Designed and built a personal portfolio site to showcase projects, resume, and contact links. Emphasized clean UI, responsiveness, and accessibility.
              
🔗 [Link](https://with-sanya.streamlit.app/)
""")

st.divider()

st.markdown("""
### 📚 Reader Room  
**🧰 Tech Stack:** HTML, NextJS, Tailwind CSS
- Designed and developed a React based frontend using Material UI and Tailwind CSS.
- Built a secure Restful API with Node.js and Express.js to handle product listings, user authentication and transaction.
- Integrated SQLite for efficient data management.             

""")
st.divider()

st.markdown("""
### 🕰️ Pomodoro Timer App
**🧰 Tech Stack:** Python, Streamlit
- Designed and developed a simple Pomodoro Timer App to make sure productivity is enhanced
- Still in development, adding more features like to do lists etc.              

""")
