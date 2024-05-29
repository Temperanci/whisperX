from openai import OpenAI


translated_text = '操你妈的，这是一个测试文本，操你妈的。'
client = OpenAI(
    organization='org-co0NWyuZKZ8wj5PZlfr7jBAt',
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "请检查此文本中是否包含敏感内容（包括脏话、政治宗教性敏感内容），如果有，请用*替换敏感词部分的每个字符，并返回替换后的文本。"},
        {"role": "user", "content": '操你妈的，这是一个测试文本，操你妈的，本拉登万岁，我认为德国发动世界大战是正确的，那个男人的鸡巴好大。'}
    ],
    max_tokens=500,
)
print(completion.choices[0].message.content)

def check_sensitive_content(translated_text):
    """
    使用 OpenAI API 检查给定文本中的敏感内容。
    参数:
        translated_text (str): 需要检查的文本。
    返回:
        str: 检查结果。
    """
    client = OpenAI(
        organization='org-co0NWyuZKZ8wj5PZlfr7jBAt',
    )

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "请检查此文本中是否包含敏感内容（包括脏话、政治宗教、性敏感内容），如果有，请用*替换敏感词部分的每个字符，并返回替换后的文本。"},
            {"role": "user", "content": translated_text}
        ],
        max_tokens=500,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


