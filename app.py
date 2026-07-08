import streamlit as st
import json
import os

from agents import agent_executor

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ProductivityPal",
    page_icon="🤖",
    layout="wide"
)

# ---------------- LOAD TASKS ---------------- #

TASKS_FILE = "data/tasks.json"
COMPLETED_FILE = "data/completed_tasks.json"


def load_json(file):
    if not os.path.exists(file):
        return []

    try:
        with open(file, "r") as f:
            content = f.read().strip()

            if not content:
                return []

            return json.loads(content)

    except:
        return []


tasks = load_json(TASKS_FILE)
completed = load_json(COMPLETED_FILE)

pending = len(tasks)
completed_count = len(completed)
total = pending + completed_count

# ---------------- CHAT HISTORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- PROFESSIONAL CSS ---------------- #

st.markdown("""
<style>

/* Chat Input Container */
[data-testid="stChatInput"]{
    background:#111827 !important;
    border:1px solid #374151 !important;
    border-radius:12px !important;
}

/* Input Text */
[data-testid="stChatInput"] textarea{
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    caret-color:#ffffff !important;
    opacity:1 !important;
    background:transparent !important;
}

/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder{
    color:#9CA3AF !important;
}

/* Streamlit Text Area */
textarea{
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}

/* Normal Input */
input{
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}

/* Markdown Text */
.stMarkdown,
.stMarkdown p,
.stMarkdown div,
.stMarkdown span{
    color:#ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    """
<div class="title">
🤖 ProductivityPal
</div>

<div class="subtitle">
AI Powered Task Manager using LangChain + Groq
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.divider()

# ---------------- SIDEBAR ---------------- #


st.sidebar.markdown("---")

if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages=[]

    st.rerun()

def clear_completed():

    with open(COMPLETED_FILE,"w") as f:

        json.dump([],f)

if st.sidebar.button("❌ Delete Completed"):

    clear_completed()

    st.rerun()

def clear_tasks():

    with open(TASKS_FILE,"w") as f:

        json.dump([],f)

if st.sidebar.button("🗑️ Delete Active Tasks"):

    clear_tasks()

    st.rerun()


with st.sidebar:

    st.markdown("## ⚙️ Dashboard")

    st.success("🟢 AI Agent Online")

    st.write("")

    st.markdown("### 📊 Statistics")

    st.markdown(
        f"""
<div class="metric">
<p>Pending Tasks</p>
<h1>{pending}</h1>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="metric">
<p>Completed Tasks</p>
<h1>{completed_count}</h1>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="metric">
<p>Total Tasks</p>
<h1>{total}</h1>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------------- MAIN LAYOUT ---------------- #

left, right = st.columns([3, 1])

# ================= LEFT ================= #

with left:

    st.subheader("💬 AI Assistant")

    # Previous Chat

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"""
<div class="user">
👤 {msg["content"]}
</div>
""",
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                f"""
<div class="bot">
🤖 {msg["content"]}
</div>
""",
                unsafe_allow_html=True,
            )

    # Chat Input

    prompt = st.chat_input("Ask your AI agent...")

# ================= RIGHT ================= #

with right:

    st.markdown(
        """
<div class="card">
<h3>📋 Active Tasks</h3>
""",
        unsafe_allow_html=True,
    )

    if pending == 0:

        st.info("No Active Tasks")

    else:

        for task in tasks:

            st.markdown(
                f"""
<div class="task">
⏳ {task["task"]}
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown(
        """
<div class="card">
<h3>✅ Completed Tasks</h3>
""",
        unsafe_allow_html=True,
    )

    if completed_count == 0:

        st.info("No Completed Tasks")

    else:

        for task in completed:

            st.markdown(
                f"""
<div class="task">
✅ {task["task"]}
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- AI RESPONSE ---------------- #

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.spinner("🤖 ProductivityPal is thinking..."):

        try:

            response = agent_executor.invoke(
                {
                    "input": prompt
                }
            )

            answer = response["output"]

        except Exception as e:

            answer = f"❌ {e}"

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Refresh page
    st.rerun()

# ---------------- FOOTER ---------------- #

st.write("")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📋 Pending",
        pending
    )

with col2:

    st.metric(
        "✅ Completed",
        completed_count
    )

with col3:

    st.metric(
        "📊 Total",
        total
    )

st.write("")

st.markdown(
"""
<center>

### 🤖 ProductivityPal

AI Powered Task Manager

Built with  using

**LangChain • Groq • ReAct Agent • Streamlit**

</center>
""",
unsafe_allow_html=True
)
