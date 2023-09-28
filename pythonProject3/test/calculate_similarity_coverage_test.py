import difflib

def calculate_similarity(original_text, copied_text):
    d = difflib.Differ()
    original_lines = original_text.splitlines()
    copied_lines = copied_text.splitlines()

    # 使用库计算两个文本的差异
    diff = list(d.compare(original_lines, copied_lines))

    # 计算相似度，忽略空行
    total_chars = sum(len(line) for line in original_lines if line.strip())
    diff_chars = sum(len(line) for line in diff if line.startswith('  '))
    similarity = (1 - (diff_chars / total_chars)) * 100

    return round(similarity, 2)
