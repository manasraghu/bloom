import streamlit as st
import sqlite3
import calendar
from datetime import datetime, timedelta

st.set_page_config(page_title="habit tracker", layout="wide")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .stApp { background: transparent; }

  .habit-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #a8c5a0;
    text-align: center;
    margin-bottom: 0.6rem;
    font-family: 'DM Sans', sans-serif;
  }

  .habit-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.5rem;
    text-align: center;
    color: #e8e0d0;
    margin: 0 0 0.5rem;
  }

  .habit-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 1.5rem 0;
  }

  .habit-header {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #4a7a6a;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
  }

  .habit-date {
    font-size: 0.65rem;
    color: #2a4a3a;
    font-family: 'DM Sans', sans-serif;
    margin-top: 0.1rem;
  }

  .habit-name {
    font-size: 0.88rem;
    color: #c9b06a;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    padding-top: 6px;
  }

  div.stButton > button {
    background-color: transparent !important;
    color: #a8c5a0 !important;
    border: 1px solid #1e3a52 !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    padding: 0.3rem 0.8rem !important;
  }

  div.stButton > button:hover {
    border-color: #a8c5a0 !important;
    color: #a8c5a0 !important;
  }

  input {
    background-color: #112236 !important;
    color: #e8e0d0 !important;
    border: 1px solid #1e3a52 !important;
    border-radius: 8px !important;
  }

  div[data-testid="stCheckbox"] {
    margin-top: -4px;
  }
</style>

<p class="habit-eyebrow">bloom — build consistency</p>
<h1 class="habit-title">habit tracker</h1>
<hr class="habit-divider">
""", unsafe_allow_html=True)


# CREATING DATABASE
conn = sqlite3.connect("habits.db")
c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS habits( 
    habit TEXT,
    date TEXT,
    completed INTEGER
          )"""
)

c.execute("""
          CREATE TABLE IF NOT EXISTS habit_names 
          (habit TEXT)
          """)

conn.commit()

if "week_offset" not in st.session_state:
    st.session_state.week_offset = 0

# DISPLAYING HABITS TABLE

today = datetime.now()
weekday = today.weekday()
monday = today - timedelta(days=weekday) + timedelta(days=st.session_state.week_offset * 7)
week_dates = [monday + timedelta(days=i) for i in range(7)]

week_label = f"{monday.strftime('%b %d')} — {week_dates[6].strftime('%b %d, %Y')}"
st.markdown(f"<p style='text-align:center; font-size:0.85rem; color:#4a7a6a; font-family:DM Sans,sans-serif; margin-bottom:1rem;'>{week_label}</p>", unsafe_allow_html=True)

cols = st.columns([4] + [3] * 9)
day_names = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

cols[0].markdown("<p class='habit-header'>Habits</p>", unsafe_allow_html=True)

# PREV BUTTON 
if cols[1].button("<-"):
    st.session_state.week_offset -= 1

# HEADERS 
for i, day in enumerate(day_names):
     cols[i + 2].markdown(f"""
    <p class='habit-header'>{day}</p>
    <p class='habit-date'>{week_dates[i].strftime('%b %d')}</p>
    """, unsafe_allow_html=True)

#NEXT BUTTON
if cols[9].button("->"):
    st.session_state.week_offset += 1

st.markdown("<hr class='habit-divider'>", unsafe_allow_html=True)

if "habits" not in st.session_state:
    st.session_state.habits = ["EXERCISE", "STUDYING", "SLEEP", "MEDITATE", "CALORIE DEFICIT", "READING"]

c.execute("SELECT * from habit_names")
names = c.fetchall()

for row in names:
    if row[0] not in st.session_state.habits:
        st.session_state.habits.append(row[0])


placeholder = ", ".join(["?" for _ in week_dates])
c.execute(f"SELECT * from habits WHERE date IN ({placeholder})",
          [d.strftime("%Y-%m-%d") for d in week_dates])

rows_from_db = c.fetchall()
conn.commit()

results = set()
for r in rows_from_db:
    results.add((r[0], r[1]))

# HABIT ROWS
for i, habit in enumerate(st.session_state.habits):
    rows = st.columns([4] + [3] * 9)
    rows[0].markdown(f"<p class='habit-name'>{habit}</p>", unsafe_allow_html=True)
    for day in range(2, 9):
        date_str = week_dates[day-2].strftime("%Y-%m-%d")
        is_completed = (habit, date_str) in results
        checked = rows[day].checkbox(
            "✔️", key=f"done_{i}_{day}_{date_str}", value=is_completed)
        
        # SAVE CHECKBOX TO DATABASE
        
        if checked is True:
            c.execute("SELECT * FROM habits WHERE habit = ? AND date = ?", (habit, date_str))
            exists = c.fetchone()
            if exists is None:
                c.execute("INSERT INTO habits VALUES(?, ?, ?)", (habit, date_str, 1))
                conn.commit()
            
        else:
            c.execute("DELETE FROM habits WHERE habit = ? AND date = ?", (habit, date_str))
            conn.commit()

# NEW HABIT ADD
c1, c2 = st.columns([0.2, 1])
with c1:
    new_habit = st.text_input("")

with c2:
    st.markdown("<div style='margin-top:28px;'>", unsafe_allow_html=True)
    if st.button("add habit"):
        if new_habit:
            st.session_state.habits.append(new_habit)
            c.execute("INSERT INTO habit_names VALUES(?)", (new_habit,))
            conn.commit()
    
    st.markdown("</div>", unsafe_allow_html=True)

        












