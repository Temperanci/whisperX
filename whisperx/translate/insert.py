# 用于插入翻译后的中文文本到ASS字幕文件中，保留原始文件的头部信息。
# 用法：将ASS文件和翻译文本文件放在同一目录下，然后运行此脚本。
# 生成的新文件名为原文件名加上'_ch-jp'后缀。

def parse_ass_line(line):
    """解析ASS字幕行，返回时间戳和文本。"""
    parts = line.split(',', 9)
    if len(parts) < 10:
        return None, None
    start_time = parts[1]
    end_time = parts[2]
    text = parts[9]
    return (start_time, end_time, text)

def insert_translation_with_header_preserved(ass_filename, txt_filename, output_filename):
    # 读取翻译文本
    with open(txt_filename, 'r', encoding='utf-8') as txt_file:
        translations = [line.strip() for line in txt_file.readlines()]

    translation_index = 0  # 用于跟踪翻译列表中的当前位置

    # 读取并处理ASS文件
    with open(ass_filename, 'r', encoding='utf-8') as ass_file:
        lines = ass_file.readlines()

    with open(output_filename, 'w', encoding='utf-8') as out_file:
        for line in lines:
            out_file.write(line)  # 直接写入当前行，包括头部信息和非对话行
            if line.startswith("Dialogue:"):
                # 确保不会因为翻译数量不足而出错
                if translation_index < len(translations):
                    # 获取当前对话的时间信息等，用于构建翻译行
                    parts = line.split(',', 9)
                    if len(parts) >= 10:  # 确保行格式正确
                        # 使用相同的时间戳和样式构建翻译行
                        translated_line = ','.join(parts[:9]) + ',' + translations[translation_index] + '\n'
                        out_file.write(translated_line)
                        translation_index += 1  # 移动到下一条翻译

# 使用示例
ass_filename = r'G:\Video\else\rio\東城りおプロが女性Mリーガーの麻雀スタイルを徹底分析!【麻雀遊戯グラフ】.ass'  # 这里替换为您的ASS文件名
txt_filename = r'G:\Video\else\rio\zh.Ys.東城りおプロが女性Mリーガーの麻雀スタイルを徹底分析!【麻雀遊戯グラフ】_text-only.txt'  # 这里替换为您的翻译TXT文件名
output_filename = f'{ass_filename[:-4]}_ch-jp.ass'  # 生成的新文件名

insert_translation_with_header_preserved(ass_filename, txt_filename, output_filename)
