from litellm import completion
from config import OPENAI_API_KEY

from litellm.exceptions import RateLimitError

def load_prompt():
    with open("prompts/travel_prompt.txt", "r") as file:
        return file.read()

def ask_travel_assistant(user_input):
    # Check for location-based request
    if user_input.lower().startswith("suggest places in"):
        country = user_input.lower().replace("suggest places in", "").strip()
        
        return f"Here are some popular places to visit in {country.title()}:\n1. Place A\n2. Place B\n3. Place C\n\nFor more detailed recommendations, please specify your interests or preferences."

    prompt = load_prompt()
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ]

    try:
        response = completion(
            model="gpt-4o-mini",  # or "gpt-4"
            messages=messages,
            api_key=OPENAI_API_KEY
        )
        return response["choices"][0]["message"]["content"]

    except RateLimitError as e:
        return "⚠️ API rate limit exceeded. Please check your OpenAI quota or billing."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"
