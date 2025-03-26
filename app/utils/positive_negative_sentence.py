import openai

openai.api_key = "your_api_key"

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Analyze sentiment and return 'positive' or 'negative'."},
            {"role": "user", "content": text}
        ]
    )
    return response["choices"][0]["message"]["content"]
