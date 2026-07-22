import streamlit as st
import time

st.set_page_config(page_title="study timer", layout="wide")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .stApp { background: transparent; }

  .timer-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #a8c5a0;
    text-align: center;
    margin-bottom: 0.6rem;
    font-family: 'DM Sans', sans-serif;
  }

  .timer-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.5rem;
    text-align: center;
    color: #e8e0d0 !important;
    margin: 0 0 0.5rem;
  }

  .timer-describe {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.1rem !important;
    text-align: center;
    color: #c9b06a !important;
    margin-bottom: 0.5 rem;
    letter-spacing: 0.05em;
            }

  .timer-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 2rem 0;
  }

  .timer-phase {
    font-family: 'DM Serif Display', serif;
    font-size: 2.5rem !important;
    text-align: center;
    color: #c9b06a;
    margin-bottom: 0.5rem;
    letter-spacing: 0.05em;
  }

  .timer-display {
    font-family: 'DM Serif Display', serif;
    font-size: 7rem !important;
    text-align: center;
    color: #e8e0d0;
    margin: 0.5rem 0 1.5rem;
    letter-spacing: 0.05em;
  }

  div.stButton > button {
    background-color: transparent !important;
    color: #a8c5a0 !important;
    border: 1px solid #1e3a52 !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.5rem !important;
    height: 45px !important;
    width: auto !important;
    min-width: 100px !important;
    letter-spacing: 0.05em !important;
  }

  div.stButton > button:hover {
    border-color: #a8c5a0 !important;
    color: #a8c5a0 !important;
  }
</style>

<p class="timer-eyebrow">bloom — stay focused</p>
<h1 class="timer-title">pomodoro timer</h1>
<h2 class="timer-describe">the pomodoro method is a time mangement technique where you work in focused 25-minute intervals, 
            followed by a 5-minute break!</h2>
<hr class="timer-divider">
""", unsafe_allow_html=True)

if "phase" not in st.session_state:
    st.session_state.phase = "work"

if "work_left" not in st.session_state:
    st.session_state.work_left = 25 * 60

if "work_running" not in st.session_state:
    st.session_state.work_running = False

if "break_left" not in st.session_state:
    st.session_state.break_left = 5 * 60

if "break_running" not in st.session_state:
    st.session_state.break_running = False

# WORK TIMER
st.markdown("<p class='timer-phase'>work</p>", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns([4, 1, 1, 1, 4])
with c2:
    if st.button("start", key="work_start"):
        st.session_state.work_running = True
with c3:
    if st.button("pause", key="work_pause"):
        st.session_state.work_running = False
with c4:
    if st.button("reset", key="work_reset"):
        st.session_state.work_running = False
        st.session_state.work_left = 25 * 60
        st.session_state.phase = "work"

mm = st.session_state.work_left // 60
ss = st.session_state.work_left % 60
st.markdown(f"<p class='timer-display'>{mm:02d}:{ss:02d}</p>", unsafe_allow_html=True)

if st.session_state.work_running and st.session_state.work_left > 0:
    time.sleep(1)
    st.session_state.work_left -= 1
    st.rerun()
elif st.session_state.work_running and st.session_state.work_left == 0:
    if st.session_state.phase == "work":
        st.session_state.phase = "break"
        st.session_state.work_left = 5 * 60
    else:
        st.session_state.phase = "work"
        st.session_state.work_left = 25 * 60
    st.rerun()

st.markdown("<hr class='timer-divider'>", unsafe_allow_html=True)

# BREAK TIMER
st.markdown("<p class='timer-phase'>break</p>", unsafe_allow_html=True)

b1, b2, b3, b4, b5 = st.columns([4, 1, 1, 1, 4])
with b2:
    if st.button("start", key="break_start"):
        st.session_state.break_running = True
with b3:
    if st.button("pause", key="break_pause"):
        st.session_state.break_running = False
with b4:
    if st.button("reset", key="break_reset"):
        st.session_state.break_running = False
        st.session_state.break_left = 5 * 60

mm_b = st.session_state.break_left // 60
ss_b = st.session_state.break_left % 60
st.markdown(f"<p class='timer-display'>{mm_b:02d}:{ss_b:02d}</p>", unsafe_allow_html=True)

if st.session_state.break_running and st.session_state.break_left > 0:
    time.sleep(1)
    st.session_state.break_left -= 1
    st.rerun()
