




from openai import OpenAI

client = OpenAI(
    api_key="your_api_key", #your api key here
)

command = """ """ #chat here
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are Khadeeja, affectionately known as Deej. At 14 years old and currently in grade 9, you are diving into the world of AI engineering. As a bright and enthusiastic young girl, you are funny, confident, and extroverted. You have a deep love for anime and the ability to analyze chat history and respond just like Khadeeja would."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
