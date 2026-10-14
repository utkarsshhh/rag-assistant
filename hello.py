from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-mini",
    max_completion_tokens=600,
    messages=[
        {"role": "system", "content": "You are a pirate."},
        {"role": "user", "content": "Explain what an AI agent is in 3 sentences."},
    ],
)

print(response.choices[0].message.content)
print("\n--- usage ---")
print(response.usage)
print ("------------------------")
print("finish_reason:", response.choices[0].finish_reason)
print("reasoning tokens:", response.usage.completion_tokens_details.reasoning_tokens)