from openai import OpenAI
import easygui

client = OpenAI(
    base_url="https://api.openai.com/v1/",
    api_key="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",
)

content = easygui.enterbox("请输入内容")

choose_model = easygui.choicebox("请选择模型", choices=["gpt-3.5-turbo", "gpt-4"])

chat_completion = client.chat.completions.create(
    model=choose_model,
    messages=[
        {"role": "system", "content": content},
    ]
)


result = chat_completion.choices[0].message.content

easygui.msgbox(result)