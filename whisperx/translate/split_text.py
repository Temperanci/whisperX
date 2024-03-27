def split_text_into_chunks(text, max_token_per_chunk):
    chunks = []
    current_chunk = ''
    token_count = 0

    # 按换行符分割文本
    lines = text.split('\n')

    for line in lines:
        # 计算当前行的 token 数量（假设每个字符都是一个 token）
        line_token_count = len(line)

        # 检查当前行的 token 数量是否超过最大限制
        if token_count + line_token_count > max_token_per_chunk:
            # 如果超过了最大限制，则将当前块添加到结果列表中，并重置当前块和 token 计数器
            chunks.append(current_chunk)
            current_chunk = ''
            token_count = 0

        # 将当前行添加到当前块中，并更新 token 计数器
        current_chunk += line + '\n'
        token_count += line_token_count

    # 将最后一个块添加到结果列表中
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def split_text_into_lines(text):
    # 直接按换行符分割文本，每行作为一个块
    lines = text.split('\n')

    # 过滤掉空行（如果需要的话）
    lines = [line for line in lines if line]

    return lines
