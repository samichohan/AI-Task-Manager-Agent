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

html,body,.stApp{

background:#09090B;
color:white;

}
            
[data-testid="collapsedControl"]{

    color:white !important;
    background:#2563EB !important;

    border-radius:10px;

    padding:8px;

    opacity:1 !important;

}

/* Chat Input Box Background */
[data-testid="stChatInput"] textarea {
    background-color: #1F2937 !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: white !important;
}




/* Sidebar */

section[data-testid="stSidebar"]{

background:#111827;
border-right:1px solid #222;

}

section[data-testid="stSidebar"] *{
    color:white !important;
}

section[data-testid="stSidebar"] button{
    color:white !important;
}

/* Hide Streamlit */

#MainMenu{
background:transparent;
}

footer{
background:transparen;
}

header{
background:transparent;
}

/* Title */

.title{

font-size:42px;
font-weight:700;
color:white;

}

.subtitle{

color:#94A3B8;
font-size:18px;

}

/* Cards */

.card{

background:#111827;

padding:22px;

border-radius:18px;

border:1px solid #333;

margin-bottom:20px;

box-shadow:0px 0px 20px rgba(0,0,0,.35);

color:white;

}

/* Metrics */

.metric{

background:transparent;

padding:18px;

border-radius:14px;

text-align:center;

margin-bottom:18px;

}

.metric h1{

color:white;

margin:0;

}

.metric p{

color:#94A3B8;

}

/* Chat */

.user{

background:#2563EB;

padding:15px;

border-radius:12px;

margin:10px 0;

color:white !important;

}

.bot{

background:#1F2937;

padding:15px;

border-radius:12px;

margin:10px 0;

color:white !important;

border:1px solid #333;

}

/* Task */

.task{

background:#1F2937;

padding:12px;

border-radius:10px;

margin-bottom:10px;

color:white !important;

font-size:16px;

border:1px solid #333;

}
/* ================= CHAT INPUT ================= */

[data-testid="stChatInput"] textarea{
    color:#FFFFFF !important;
    -webkit-text-fill-color:#FFFFFF !important;
    caret-color:#FFFFFF !important;
}

[data-testid="stChatInput"] textarea::placeholder{
    color:#9CA3AF !important;
}

[data-testid="stChatInput"]{
    background:#111827 !important;
    border:1px solid #333 !important;
    border-radius:12px !important;
}

/* Scroll */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:transparent;

border-radius:20px;

}

h1,h2,h3,h4,h5,h6,p,span,div{
    color:white !important;
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

Built with ❤️ using

**LangChain • Groq • ReAct Agent • Streamlit**

</center>
""",
unsafe_allow_html=True
)
