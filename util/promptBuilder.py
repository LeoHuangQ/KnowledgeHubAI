from api.OpenAIClient import client

def build_prompt(questions, context):
    prompt = f"You are a helpful AI assistant. Answer the user's question using ONLY the provided context. If the answer cannot be found in the context, say: 'I don't have enough information to answer that.' Answer the following questions based on the provided context:\n\nContext:\n{context}\n\nQuestions:\n"
    for i, question in enumerate(questions):
        prompt += f"{i + 1}. {question}\n"
    prompt += "\nPlease provide detailed answers to each question."
    return prompt

async def stream_answer(prompt):
    stream = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta