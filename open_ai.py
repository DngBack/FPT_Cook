from openai import OpenAI
client = OpenAI(api_key="")

content = """
Write code for read file txt
"""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": content
        }
    ]
)

print(completion.choices[0].message.content)