import streamlit as st
from PIL import Image

st.set_page_config(page_title="meditation", layout="wide")

mindfulness = Image.open("pics/mindful.png")
mantra = Image.open("pics/mantra.png")
bodyscan = Image.open("pics/body.png")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .med-wrap {
    background: transparent;
    padding: 2rem 2.5rem 4rem;
    font-family: 'DM Sans', sans-serif;
    color: #e8e0d0;
  }
  .med-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #a8c5a0;
    text-align: center;
    margin-bottom: 0.6rem;
  }
  .med-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.5rem;
    text-align: center;
    color: #e8e0d0;
    margin: 0 0 0.8rem;
  }
  .med-subtitle {
    text-align: center;
    font-size: 0.9rem;
    color: #6a8a7a;
    max-width: 700px;
    margin: 0 auto 2rem;
    line-height: 1.7;
    font-style: italic;
  }
  .med-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 2rem 0;
  }
  .med-section-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #4a7a6a;
    text-align: center;
    margin-bottom: 1.5rem;
  }
  .med-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin-top: 1rem;
  }
  .med-card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.2rem;
    color: #a8c5a0;
    margin: 1rem 0 0.6rem;
  }
  .med-card-desc {
    font-size: 0.82rem;
    color: #6a8a7a;
    line-height: 1.7;
  }
</style>

<div class="med-wrap">
  <p class="med-eyebrow">bloom — self care</p>
  <h1 class="med-title">meditation</h1>
  <p style='text-align: center; colour: #6a8a7a !important;'>take a break from studying and relax your mind.</p>
  <hr class="med-divider">
</div>
""", unsafe_allow_html=True)

# CENTERED VIDEO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.video("https://youtu.be/inpok4MKVLM?si=CtFnwpWKSbsTOaA1")

st.markdown("""
<div class="med-wrap" style="padding-top: 1rem;">
  <hr class="med-divider">
  <p class="med-section-label">types of meditation</p>
  <p style='text-align: center; color: #6a8a7a;'>below are the most common types of meditation. see what best suits you!</p>
</div>
""", unsafe_allow_html=True)

# 3 CARDS WITH IMAGES ON TOP
col1, col2, col3 = st.columns(3)

with col1:
    st.image(mindfulness, use_container_width=True)
    st.markdown("""
    <div class="med-card-title">Mindfulness Meditation</div>
    <div class="med-card-desc">focus your attention on the present moment — your breathing, thoughts, and surroundings — without judgement. when your mind wanders, gently bring it back. builds awareness and reduces stress over time.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(mantra, use_container_width=True)
    st.markdown("""
    <div class="med-card-title">Mantra Meditation</div>
    <div class="med-card-desc">silently or softly repeat a word, phrase, or sound (like "om") to anchor your focus. the repetition quiets mental chatter and brings you into a calm, centred state.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image(bodyscan, use_container_width=True)
    st.markdown("""
    <div class="med-card-title">Body Scan Meditation</div>
    <div class="med-card-desc">slowly move your attention from the top of your head down to your feet, noticing any tension, discomfort, or sensation in each part of your body. helps release physical tension and builds a stronger mind-body connection.</div>
    </div>
    """, unsafe_allow_html=True)
