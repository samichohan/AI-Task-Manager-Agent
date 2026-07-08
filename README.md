# 🤖 ProductivityPal – AI Task Manager

An AI-powered Task Management Assistant built with **LangChain**, **Groq Llama 3.3**, and **Streamlit**.

This project uses a ReAct Agent that can understand natural language, decide which tool to use, and manage tasks intelligently with both short-term and long-term memory.

---

## 🚀 Live Demo

👉 **Live App:** https://YOUR-STREAMLIT-LINK.streamlit.app

---

## 📸 Preview

> Add screenshots of your application here.

| Dashboard | Chat |
|-----------|------|


---

# ✨ Features

- 🤖 AI Task Management Assistant
- 🧠 ReAct Agent (Reason + Act)
- 💬 Natural Language Task Management
- 📌 Add Tasks
- 📋 View Active Tasks
- ✅ Complete Tasks
- 📂 View Completed Tasks
- 🧹 Clear Chat
- 🗑 Delete Active Tasks
- ❌ Delete Completed Tasks
- 💾 Long-Term Memory using JSON
- 🧠 Short-Term Conversation Memory
- 🌙 Professional Dark UI
- ⚡ Fast Responses with Groq Llama 3.3

---

# 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Llama 3.3 70B
- JSON Storage

---

# 📂 Project Structure

```
ProductivityPal/
│
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── .env
│
├── data/
│   ├── tasks.json
│   └── completed_tasks.json
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/samichohan/AI-Task-Manager-Agent.git
```

Go into the project

```bash
cd ProductivityPal
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 💬 Example Commands

```
Add a task to learn LangChain tomorrow

Show my tasks

Complete task 1

Show completed tasks

Delete all completed tasks

Delete all active tasks
```

---

# 🧠 How It Works

1. User sends a message.
2. The LangChain ReAct Agent analyzes the request.
3. The agent selects the appropriate tool.
4. The tool performs the action.
5. The response is returned to the user.
6. Chat history is stored in memory.
7. Tasks are stored in JSON files for persistence.

---

# 🔧 Available Tools

- Add Task
- View Tasks
- Complete Task
- View Completed Tasks

---

# 📚 Concepts Used

- ReAct Agent
- Tool Calling
- Agent Executor
- Prompt Engineering
- Short-Term Memory
- Long-Term Memory
- LangChain Tools
- Streamlit UI

---

# 🎯 Future Improvements

- Edit Tasks
- Task Priority
- Due Dates
- SQLite Database
- User Authentication
- Cloud Database
- Email Reminders
- Multi-Agent Workflow
- Voice Assistant
- Calendar Integration

---

# 👨‍💻 Author

**Sami Chohan**

AI & Data Science Student

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.