def summarize_text(text, client):
    """Generate a summary of the provided text using OpenAI's GPT-4 chat model."""
    try:
        # Using the chat completions endpoint for GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Please summarize the following text:"},
                {"role": "user", "content": text}
            ],
            max_tokens=150
        )
        # Accessing the text from the first completion choice
        return response.choices[0].message.content.strip() if response.choices else "No summary available."
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
