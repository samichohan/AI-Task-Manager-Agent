from agent import agent_executor

def run():
    print(" ProductivityPal Started! (type 'exit' to quit)\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = agent_executor.invoke({"input": user_input})
        print(f"\nBot: {response['output']}\n")

if __name__ == "__main__":
    run()