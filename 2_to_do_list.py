import streamlit as st 

st.set_page_config(page_title="to-do list", layout="wide")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

  .stApp { background: transparent; }

  input {
    background-color: #112236 !important;
    color: #e8e0d0 !important;
    border: 1px solid #1e3a52 !important;
    border-radius: 8px !important;
  }

  div[data-testid="stCheckbox"] {
    margin-top: -20px;
}

  div[data-baseweb="select"] {
    background-color: #112236 !important;
    border: 1px solid #1e3a52 !important;
    border-radius: 8px !important;
    color: #e8e0d0 !important;
  }

  div.stButton > button {
    background-color: #a8c5a0 !important;
    color: #0d1b2a !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.5rem !important;
    letter-spacing: 0.05em !important;
  }

  div.stButton > button:hover {
    background-color: #8fb387 !important;
    color: #0d1b2a !important;
  }

  .todo-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #a8c5a0;
    text-align: center;
    margin-bottom: 0.6rem;
    font-family: 'DM Sans', sans-serif;
  }

  .todo-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.5rem;
    text-align: center;
    color: #e8e0d0;
    margin: 0 0 0.5rem;
  }

  .todo-divider {
    border: none;
    border-top: 1px solid #1e3a52;
    margin: 1.5rem 0;
  }

  .todo-header {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #4a7a6a;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
  }

  .todo-input-label {
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #6a8a7a;
    font-family: 'DM Sans', sans-serif;
    margin-bottom: 0.3rem;
  }

  .priority-high { color: #c9a0a0; font-size: 0.82rem; }
  .priority-medium { color: #c9b06a; font-size: 0.82rem; }
  .priority-low { color: #a8c5a0; font-size: 0.82rem; }
</style>

<p class="todo-eyebrow">bloom — stay organised</p>
<h1 class="todo-title">to-do list</h1>
<hr class="todo-divider">
""", unsafe_allow_html=True)

# ROW 1 - INPUT FIELDS
c1, c2, c3, c4 = st.columns([2, 3, 1.5, 1.5])
with c1:
    subj = st.text_input("subject")
with c2:
    task = st.text_input("task")
with c3:
    date = st.text_input("due date")
with c4:
    priority = st.selectbox(
        label = "priority",
        options = ["high", "medium", "low"]
)

# ROW 2 - ADD TASK BUTTON 
st.markdown("<div style='margin-top: 0.5rem;'>", unsafe_allow_html=True)
if st.button("add task"):
        st.session_state.tasks.append({
            "subject" : subj,
            "task" : task,
            "due date" : date,
            "priority" : priority
        })

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr class='todo-divider'>", unsafe_allow_html=True)


# ROW 3 - HEADERS
col1, col2, col3, col4, col5 = st.columns([2, 3, 1, 1, 1])
# | subject | task | duedate | priority | checkbox |
col1.markdown("<p class='todo-header'>Subject</p>", unsafe_allow_html=True)
col2.markdown("<p class='todo-header'>Task</p>", unsafe_allow_html=True)
col3.markdown("<p class='todo-header'>Due Date</p>", unsafe_allow_html=True)
col4.markdown("<p class='todo-header'>Priority</p>", unsafe_allow_html=True)
col5.markdown("<p class='todo-header'>Done</p>", unsafe_allow_html=True)

# ROW 4 - TASK ROWS
for i, task in enumerate(st.session_state.tasks):
     c1, c2, c3, c4, c5 = st.columns([2, 3, 1, 1, 1])
     c1.write(task["subject"])
     c2.write(task["task"])
     c3.write(task["due date"])
     c4.write(task["priority"])
     c5.checkbox("done", key = f"done_{i}", label_visibility="hidden")