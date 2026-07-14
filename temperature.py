from openai import OpenAI
client = OpenAI(
    api_key="os.gentenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
prompt = "Explain Python in simple words."
temperatures = [0.0, 0.3, 0.7, 1.0]
for temp in temperatures:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temp,
        max_tokens=300
    )
    print("=" * 50)
    print(f"Temperature: {temp}")
    print(response.choices[0].message.content)
