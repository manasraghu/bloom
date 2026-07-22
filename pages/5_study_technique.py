import streamlit as st
from PIL import Image

st.set_page_config(page_title="study techniques", layout="wide")

# IMAGES
active_recall = Image.open("pics/act_rec.png")
pomodoro = Image.open("pics/pomo.png")
feynman = Image.open("pics/feynman.png")
spaced_repetition = Image.open("pics/spacerep.png")
mind_map = Image.open("pics/mindmap.png")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .st-wrap {
    background: transparent;
    padding: 2rem 2.5rem 4rem;
    font-family: 'DM Sans', sans-serif;
    color: #e8e0d0;
  }
  .st-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #a8c5a0;
    text-align: center;
    margin-bottom: 0.6rem;
  }
  .st-title {
    font-family: 'DM Serif Display', serif;
    font-size: 5rem;
    text-align: center;
    color: #dbb95a !important;
    margin: 0 0 1rem;
  }
  .st-subtitle {
    text-align: center;
    font-size: 0.9rem;
    color: #6a8a7a;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
  }
  .st-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 0 0 2.5rem;
  }
  .st-technique {
    display: flex;
    gap: 2.5rem;
    align-items: flex-start;
    margin-bottom: 2.8rem;
    padding-bottom: 2.8rem;
    border-bottom: 1px solid #1a2e40;
  }
  .st-technique:last-child { border-bottom: none; }
  .st-text { flex: 1; }
  .st-technique-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    color: #a8c5a0 !important;
    margin: 0 0 0.6rem;
  }
  .st-desc {
    font-size: 0.88rem;
    color: #9aab9a;
    line-height: 1.75;
    margin-bottom: 1rem;
  }
  .st-meta { display: flex; flex-direction: column; gap: 0.3rem; }
  .st-meta-row { font-size: 0.78rem; line-height: 1.5; }
  .st-meta-label {
    color: #c9a0a0;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.7rem;
  }
  .st-meta-value { color: #7a9a8a; }
</style>

<div class="st-wrap">
  <p class="st-eyebrow">bloom — study smarter</p>
  <h1 class="st-title">study techniques</h1>
  <p class="st-subtitle">not sure how to study effectively? here are five proven methods, organised by the type of studying and subjects they suit best. try them out and see what works for you!</p>
  <hr class="st-divider">
</div>
""", unsafe_allow_html=True)

# ACTIVE RECALL
col1, col2 = st.columns((1, 2))
with col1:
    st.image(active_recall)
with col2:
    st.markdown("""
    <div class="st-text">
      <h2 class="st-technique-title">Active Recall</h2>
      <p class="st-desc">instead of passively rereading notes, you actively try to retrieve information from memory — through flashcards, practice questions, or covering your notes and recalling key points without looking. this struggle to recall strengthens memory more than passive review, since your brain has to actively search for and reconstruct the information rather than just recognising it.</p>
      <div class="st-meta">
        <div class="st-meta-row"><span class="st-meta-label">relevant subjects</span><br><span class="st-meta-value">biology, chemistry, history — any subject with discrete facts or definitions</span></div>
        <div class="st-meta-row"><span class="st-meta-label">best for</span><br><span class="st-meta-value">memorisation-heavy revision</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)

# POMODORO
col1, col2 = st.columns((1, 2))
with col1:
    st.image(pomodoro)
with col2:
    st.markdown("""
    <div class="st-text">
      <h2 class="st-technique-title">Pomodoro Technique</h2>
      <p class="st-desc">break your work into focused intervals (traditionally 25 minutes), followed by a short 5 minute break. after 4 intervals, take a longer break (15–30 minutes). the fixed time blocks create urgency and prevent burnout by forcing regular rest.</p>
      <div class="st-meta">
        <div class="st-meta-row"><span class="st-meta-label">relevant subjects</span><br><span class="st-meta-value">any subject</span></div>
        <div class="st-meta-row"><span class="st-meta-label">best for</span><br><span class="st-meta-value">staying focused during long study sessions</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)

# FEYNMAN
col1, col2 = st.columns((1, 2))
with col1:
    st.image(feynman)
with col2:
    st.markdown("""
    <div class="st-text">
      <h2 class="st-technique-title">Feynman Technique</h2>
      <p class="st-desc">explain a concept in simple, plain language as if teaching it to someone with no background knowledge. when you get stuck or use jargon to cover a gap, that's a sign you don't fully understand that part. go back, relearn it, then try explaining again.</p>
      <div class="st-meta">
        <div class="st-meta-row"><span class="st-meta-label">relevant subjects</span><br><span class="st-meta-value">math, physics, computer science, economics</span></div>
        <div class="st-meta-row"><span class="st-meta-label">best for</span><br><span class="st-meta-value">deep conceptual understanding</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)

# MIND MAP
col1, col2 = st.columns((1, 2))
with col1:
    st.image(mind_map)
with col2:
    st.markdown("""
    <div class="st-text">
      <h2 class="st-technique-title">Mind Mapping</h2>
      <p class="st-desc">start with a central topic in the middle of the page, then branch outward into subtopics, and branch further into smaller details — creating a visual web of connected ideas instead of linear notes. colour coding and images can reinforce the connections.</p>
      <div class="st-meta">
        <div class="st-meta-row"><span class="st-meta-label">relevant subjects</span><br><span class="st-meta-value">biology, history, literature</span></div>
        <div class="st-meta-row"><span class="st-meta-label">best for</span><br><span class="st-meta-value">seeing the big picture and connecting different ideas</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)

# SPACED REPETITION
col1, col2 = st.columns((1, 2))
with col1:
    st.image(spaced_repetition)
with col2:
    st.markdown("""
    <div class="st-text">
      <h2 class="st-technique-title">Spaced Repetition</h2>
      <p class="st-desc">review material at increasing intervals over time (e.g. 1 day, 3 days, 1 week, 1 month) instead of cramming everything at once. each review happens right before you'd naturally start forgetting, which reinforces the memory more efficiently than repeated short-term review.</p>
      <div class="st-meta">
        <div class="st-meta-row"><span class="st-meta-label">relevant subjects</span><br><span class="st-meta-value">medical terminology, language learning, formulas</span></div>
        <div class="st-meta-row"><span class="st-meta-label">best for</span><br><span class="st-meta-value">retaining information long after the test</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)