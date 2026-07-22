import streamlit as st

st.set_page_config(
    page_title="bloom",
    page_icon="🌿",
    layout="wide"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .bloom-wrap {
    background: transparent;
    min-height: 100vh;
    padding: 3rem 2.5rem 4rem;
    font-family: 'DM Sans', sans-serif;
    color: #e8e0d0;
  }
  .bloom-logo {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    color: #a8c5a0;
    letter-spacing: 0.02em;
    margin-bottom: 4rem;
    text-align: center;
  }
  .bloom-eyebrow {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #a8c5a0;
    margin-bottom: 1rem;
    text-align: center;
  }
  .bloom-headline {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    line-height: 1.15;
    color: #e8e0d0;
    margin: 0 0 1.2rem;
    text-align: center;
  }
  .bloom-headline span { color: #a8c5a0; }
  .bloom-quote {
    font-size: 0.95rem;
    color: #9aab9a;
    font-style: italic;
    padding-left: 1rem;
    margin-top: 1.5rem;
    line-height: 1.7;
    text-align: center;
  }
  .bloom-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 2.5rem 0;
  }
  .bloom-section-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #4a7a6a;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  .bloom-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
  }
  .bloom-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.03);
    border-radius: 12px;
    padding: 1.4rem 1.2rem;
    transition: border-color 0.2s;
  }
  .bloom-card:hover { border-color: #a8c5a0; }
  .bloom-card-icon { font-size: 1.4rem; margin-bottom: 0.75rem; text-align: center; }
  .bloom-card-title {
    font-size: 0.85rem;
    font-weight: 500;
    color: #e8e0d0;
    margin-bottom: 0.4rem;
    letter-spacing: 0.03em;
    text-align: center;
  }
  .bloom-card-desc {
    font-size: 0.78rem;
    color: #6a8a7a;
    line-height: 1.55;
    text-align: center;
  }
  .bloom-footer {
    margin-top: 3.5rem;
    font-size: 0.72rem;
    color: #2a4a3a;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }
</style>

<div class="bloom-wrap">
  <div class="bloom-logo">bloom</div>

  <p class="bloom-eyebrow">your productivity companion</p>
  <h1 class="bloom-headline">grow a little <span>every day</span></h1>
  <p class="bloom-quote">"Small daily improvements are the key to staggering long-term results." — Robin Sharma</p>

  <hr class="bloom-divider">
  <p class="bloom-section-label">what's inside</p>

  <div class="bloom-cards">
    <div class="bloom-card">
      <div class="bloom-card-icon">✅</div>
      <div class="bloom-card-title">To-Do List</div>
      <div class="bloom-card-desc">track tasks by subject, priority, and due date — study or miscellaneous.</div>
    </div>
    <div class="bloom-card">
      <div class="bloom-card-icon">🍅</div>
      <div class="bloom-card-title">Study Timer</div>
      <div class="bloom-card-desc">stay focused with a pomodoro-style work and break timer.</div>
    </div>
    <div class="bloom-card">
      <div class="bloom-card-icon">🌿</div>
      <div class="bloom-card-title">Habit Tracker</div>
      <div class="bloom-card-desc">log your daily habits and build streaks across the week.</div>
    </div>
    <div class="bloom-card">
      <div class="bloom-card-icon">📖</div>
      <div class="bloom-card-title">Study Techniques</div>
      <div class="bloom-card-desc">explore methods like active recall, pomodoro, and spaced repetition.</div>
    </div>
    <div class="bloom-card">
      <div class="bloom-card-icon">🧘</div>
      <div class="bloom-card-title">Self Care</div>
      <div class="bloom-card-desc">meditate, breathe, and reset with guided resources and a timer.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
