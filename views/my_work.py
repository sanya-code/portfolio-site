import streamlit as st 

st.title(" Thoughts I Gave a Plot ")
st.markdown("#### :red-background[A Little Backstory]")
st.markdown('''

#### ✍️ My Writer Origin Story (No Capes, Just Pens)
I’ve been writing for as long as I can remember — seriously, if you’ve peeked at my design page, you already know I was that kid who discovered creativity before algebra. It all started with scribbling thoughts into a diary. One diary turned into two, then four... until my mom caught on, decided my emotional outpour wasn’t part of the curriculum, and “confiscated” them in the name of academics (fair enough, I had to study too).

But did that stop me? Nope. I leveled up — from pen to keyboard. Soon, I was typing away on my laptop and posting under a mysterious little Instagram fan account. Slowly, words turned into stories, readers turned into friends, and before I knew it, I was collaborating with fellow writers and publishing our work on Instagram and, of course, the holy grail of all fanfiction dreams — Wattpad.

Since then, I’ve dabbled in all sorts of writing communities. One special mention goes to Embrace Our Desi — a global student collective connecting desi hearts across borders. I had the joy of writing and designing for them, and fun fact: I even got interviewed by a girl from L.A. (Yes, I felt like I was on a Netflix coming-of-age series).


''')



st.divider()



option = st.selectbox("Some Pieces", [
    "Of Roads, Rikshaws, and Real Riches",
    "Days of Our Lives",
    
]

)

# st.title(option)
# st.subheader("- By Sanya")

if option == "Of Roads, Rikshaws, and Real Riches":
    with open("content/story_1.py",'r') as f:
        st.markdown(f.read())


st.markdown("#### Coming Soon!")