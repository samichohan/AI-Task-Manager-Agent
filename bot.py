from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def think(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content

# Agent personality in prompt
system_prompt = """You are a simple AI agent called ThinkBot.
When given a goal, you:
1. Break it into small steps
2. Execute each step one by one
3. When done, say DONE.

Always think out loud - show your steps."""

#Agent loop
def run_agent(goal):
    print(f"\n Goal: {goal}")
    print("-" *     40)

    messages = [
        {'role':'system','content': system_prompt},
        {'role':'user','content':f"My goal: {goal}"}
    ]


    step = 1
    while True:
        response = think(messages)
        print(f"\nThinkBot Step {step}:\n{response}")

        if "DONE" in response:
            print("\nThinkBot finished!")
            break


        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": "Continue to next step."})


        step += 1

        
        if step > 5:
            print("\nMax steps reached.")
            break


# Run karo!
run_agent("Explain why sky is blue in 3 simple points")