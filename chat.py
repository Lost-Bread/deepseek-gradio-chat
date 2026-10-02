import os
from openai import OpenAI
import gradio as gr
#print(os.environ.get("DEEPSEEK_API_KEY") is not None)


client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

def chat(message,history):
    messages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

    for user_msg, assistant_msg in history:
        messages.append(
            {"role": "user", "content": user_msg}
        )
        messages.append(
            {"role": "assistant", "content": assistant_msg}
        )
        messages.append(
            {"role": "user", "content": message}
        )

       # print(messages)

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    answer = response.choices[0].message.content
    print("User：", message)
    print("AI：", answer)
    print("------------------------------")

    return answer

demo = gr.ChatInterface(
    fn=chat,
    title="MWT's AI Help Assistant",
)
demo.launch(share=True)
