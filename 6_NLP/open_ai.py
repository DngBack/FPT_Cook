from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": " starting with pe with regex in python"
        }
    ]
)

print(completion.choices[0].message.content)