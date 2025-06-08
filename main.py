# main.py
from agent import ask_travel_assistant

def main():
    print("🌍 Travel Assistant AI ✈️")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ask_travel_assistant(user_input)
        print(f"AI: {response}\n")

if __name__ == "__main__":
    main()
