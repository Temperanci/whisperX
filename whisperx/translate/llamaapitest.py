import os.path
from pathlib import Path
import requests
from .split_text import split_text_into_lines

endpoint = 'http://4kr.top:7097/v1/chat/completions'

# 读取文本文件并翻译
def translate2ch(file_path):
    fdir, fname = os.path.split(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 构造输出文件路径
    srt_file = str((Path(fdir) / fname).absolute()).replace('.txt', '.srt')

    # 按换行为界分割文本，每行作为一个分割块
    text_chunks = split_text_into_lines(text)

    print(f'分割完成！分割后的文本块数量: {len(text_chunks)}')

    def append_to_srt(data, file_path, line_number):
        translated_text = data["choices"][0]["message"]["content"].strip()

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 初始化变量用于跟踪当前行号和当前字幕序号
        current_line_number = 0
        current_subtitle_number = 0

        # 找到插入点的索引
        insert_index = None
        for i, line in enumerate(lines):
            if line.strip().isdigit():
                current_subtitle_number = int(line.strip())
                if current_subtitle_number == line_number:
                    insert_index = i
                    break
            current_line_number += 1

        if insert_index is not None:
            # 插入翻译文本和必要的时间戳和空行
            # 注意，我们需要增加所有后续字幕序号
            lines.insert(insert_index + 3, "\n")
            lines.insert(insert_index + 3, translated_text)
            lines.insert(insert_index + 3, "\n" + lines[insert_index + 1])
            lines.insert(insert_index + 3, "\n" + str(line_number))

            # 更新后续字幕的序号
            for j in range(insert_index + 7, len(lines), 4):
                if lines[j].strip().isdigit():
                    new_number = int(lines[j].strip()) + 1
                    lines[j] = str(new_number) + "\n"

        with open(file_path, 'w', encoding='utf-8') as new_file:
            new_file.writelines(lines)


    # 翻译并打印每个文本块
    line_number = 1
    for i, chunk in enumerate(text_chunks):
        print(f'第 {i+1} 个文本块翻译后的结果:')
        resp = requests.post(endpoint, json={
            "do_sample": True,
            "frequency_penalty": 0,
            "max_tokens": 1000,
            "messages": [
                {"role": "system", "content": "你是一个轻小说翻译模型，可以流畅通顺地以日本轻小说的风格将日文翻译成简体中文，并联系上下文正确使用人称代词，不擅自添加原文中没有的代词。"},
                {"role": "user", "content": "将下面的日文文本翻译成中文：" + chunk},
            ],
            "model": "sakura-13b-lnovel-v0.9b-Q6_K",
            "num_beams": 1,
            "repetition_penalty": 1,
            "temperature": 0.1,
            "top_k": 40,
            "top_p": 0.3
        })

        # 将 JSON 数据写入到输出文件中
        print(resp.json())
        append_to_srt(resp.json(), srt_file, line_number)
        line_number += 1

