import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a summarizer. Give a concise summary in bullet points. Max 5 points."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def translate(text,language):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": f"You are a translator. Translate the following text to {language}."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def sentiment(text):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": """You are a sentiment analyzer. Analyze the sentiment and return in this exact format:
Sentiment: [POSITIVE/NEGATIVE/NEUTRAL]
Confidence: [HIGH/MEDIUM/LOW]
Reason: one line explanation""" },
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content