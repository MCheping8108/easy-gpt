import os

from openai import OpenAI
import easygui
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    # 这个接口是中国的ChatGPT镜像站点，使用openai官方接口时把它改成https://api.openai.com/v1
    # 从.env加载BASE_URL和OPENAI_API_KEY
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

list_model = ["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-1106", "gpt-4", "gpt-4-0314", "gpt-4-0613", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-1106-preview", "gpt-4-vision-preview"]

content = easygui.enterbox("请输入内容")

choose_model = easygui.choicebox("请选择模型", choices=list_model)

chat_completion = client.chat.completions.create(
    model=choose_model,
    messages=[
        {"role": "system", "content": content},
    ]
)


result = chat_completion.choices[0].message.content

with open("result.md", "w") as f:
    f.write(result)