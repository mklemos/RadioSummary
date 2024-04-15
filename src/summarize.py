# summarize.py
"""
This module provides functionality to generate summaries of text using OpenAI's GPT-4 chat model.
"""

def summarize_text(text, client):
    """
    Generate a summary of the provided text using OpenAI's GPT-4 chat model.

    :param text: The text to summarize.
    :param client: An initialized instance of the OpenAI client.
    :return: A string containing the summary if successful, 'No summary available.' 
            if no summary is produced, or None if an error occurs.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Please summarize the following text:"},
                {"role": "user", "content": text}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip() if response.choices else "No summary available."

    except Exception as e:  # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None
