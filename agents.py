from langchain_groq import ChatGroq
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools import add_task, view_completed_tasks, view_tasks, complete_task

load_dotenv()

# LLM Setup ---> Brain of the agent
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tools List
tools = [add_task, view_tasks, complete_task, view_completed_tasks]

# Memory (Short-Term / Conversation) 
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Agent Prompt  ----> Reasoning + Action + Observation
template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

IMPORTANT RULES:
- If the user's request is vague or doesn't contain a clear, specific task description 
  (e.g., "I want to add a task" without saying WHAT the task is), 
  do NOT use any tool. Instead, skip directly to "Final Answer" and ask the user 
  to specify the task clearly.
- Only use a tool when you have enough clear information to do so.
- If you don't need to use a tool, go directly from Thought to Final Answer 
  (do NOT write "Action: None").

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}] (ONLY if a tool is actually needed)
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Previous conversation history:
{chat_history}

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

# Create Agent
agent = create_react_agent(llm, tools, prompt)

# Agent Executor 
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True, 
    handle_parsing_errors=True
)
