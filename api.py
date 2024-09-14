# api.py
import openai
from config import get_api_key

# Initialize the OpenAI API key
openai.api_key = get_api_key()

def get_completion(prompt):
    """
    Makes a request to the OpenAI API to get a completion for the given prompt.
    """
    try:
        completion = openai.ChatCompletion.create(
            # model="gpt-4",
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"